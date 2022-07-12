import argparse
from pathlib import Path

from analysis.src.python.evaluation.model.column_name import ColumnName
from analysis.src.python.evaluation.utils.args_util import EvaluationRunToolArgument

HYPERSTYLE_TOOL_PATH = 'hyperstyle/src/python/review/run_tool.py'

HYPERSTYLE_DOCKER_PATH = 'stepik/hyperstyle:1.2.2'


def configure_arguments(parser: argparse.ArgumentParser) -> None:

    parser.add_argument(EvaluationRunToolArgument.SOLUTIONS_FILE_PATH.value.long_name,
                        type=lambda value: Path(value).absolute(),
                        help=EvaluationRunToolArgument.SOLUTIONS_FILE_PATH.value.description)

    parser.add_argument('-dp', '--docker-path',
                        default=HYPERSTYLE_DOCKER_PATH,
                        type=lambda value: Path(value).absolute(),
                        help='Path to docker (USER/NAME:VERSION) to run evaluation on.')

    parser.add_argument('-tp', '--tool-path',
                        default=HYPERSTYLE_TOOL_PATH,
                        type=lambda value: Path(value).absolute(),
                        help='Path to script in docker to run on files.')

    parser.add_argument('--with-history',
                        help=f'If True, then history will be taken into account when calculating the grade. '
                             f'In that case, for each fragment, the "{ColumnName.HISTORY.value}" column '
                             'must contain the history of previous errors.',
                        action='store_true')

    parser.add_argument('--allow-duplicates',
                        help=f'If True, then history will be taken into account when calculating the grade. '
                             f'In that case, for each fragment, the "{ColumnName.HISTORY.value}" column '
                             'must contain the history of previous errors.',
                        action='store_true')

    parser.add_argument('--with-all-categories',
                        help=f'Without this flag, all issues will be categorized into 5 main categories: '
                             f'CODE_STYLE, BEST_PRACTICES, ERROR_PRONE, COMPLEXITY, INFO.',
                        action='store_true')
