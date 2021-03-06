import argparse
import os
import sys
from pathlib import Path

import torch
from analysis.src.python.evaluation.qodana.imitation_model.common.metric import Measurer
from analysis.src.python.evaluation.qodana.imitation_model.common.train_config import (
    configure_arguments, MultilabelTrainer, TrainingArgs,
)
from analysis.src.python.evaluation.qodana.imitation_model.common.util import DatasetColumnArgument
from analysis.src.python.evaluation.qodana.imitation_model.dataset.dataset import QodanaDataset
from transformers import RobertaForSequenceClassification


def main():
    parser = argparse.ArgumentParser()
    configure_arguments(parser)
    args = parser.parse_args()
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    train_dataset = QodanaDataset(args.train_dataset_path, args.context_length)
    val_dataset = QodanaDataset(args.val_dataset_path, args.context_length)
    train_steps_to_be_made = len(train_dataset) // args.batch_size
    val_steps_to_be_made = train_steps_to_be_made // 5
    print(f'Steps to be made: {train_steps_to_be_made}, validate each {val_steps_to_be_made}th step.')

    num_labels = train_dataset[0][DatasetColumnArgument.LABELS.value].shape[0]
    model = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=num_labels).to(device)

    metrics = Measurer(args.threshold)
    if args.trained_weights_directory_path is None:
        args.trained_weights_directory_path = Path(args.train_dataset_path).parent / DatasetColumnArgument.WEIGHTS.value
        os.makedirs(args.trained_weights_directory_path, exist_ok=True)

    train_args = TrainingArgs(args)

    trainer = MultilabelTrainer(model=model,
                                args=train_args.get_training_args(val_steps_to_be_made),
                                train_dataset=train_dataset,
                                eval_dataset=val_dataset,
                                compute_metrics=metrics.compute_metric)
    trainer.train()


if __name__ == '__main__':
    sys.exit(main())
