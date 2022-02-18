import argparse
import logging
import os
import sys
from typing import Optional

from analysis.src.python.data_analysis.model.column_name import IssuesColumns, SubmissionColumns
from analysis.src.python.data_analysis.utils.df_utils import merge_dfs, read_df
from analysis.src.python.data_analysis.utils.logging_utils import configure_logger
from analysis.src.python.evaluation.common.file_util import AnalysisExtension, create_directory


def get_issues_steps_statistics(submissions_path: str,
                                issue_statistics_path: str,
                                issues_steps_statistics_directory_path: str,
                                issues_path: str,
                                attempt_number: Optional[int]):
    """ Calculate issue count for each step. """

    df_submissions = read_df(submissions_path)

    # Select submission's attempt
    if attempt_number is not None:
        if attempt_number == -1:
            df_submissions = df_submissions[
                df_submissions[SubmissionColumns.ATTEMPT.value] == SubmissionColumns.TOTAL_ATTEMPTS.value]
        else:
            df_submissions = df_submissions[df_submissions[SubmissionColumns.ATTEMPT.value] == attempt_number]

    df_issues = read_df(issues_path)

    df_issues_statistics = read_df(issue_statistics_path)

    df_issues_statistics = merge_dfs(
        df_submissions[[SubmissionColumns.ID.value, SubmissionColumns.STEP_ID.value]],
        df_issues_statistics,
        SubmissionColumns.ID.value,
        SubmissionColumns.ID.value,
    )

    create_directory(issues_steps_statistics_directory_path)

    for issue_class in df_issues[IssuesColumns.CLASS.value].values:
        issue_stats_path = os.path.join(issues_steps_statistics_directory_path, f'{issue_class}{AnalysisExtension.CSV}')
        df_issues_statistics[[issue_class, SubmissionColumns.STEP_ID.value]][df_issues_statistics[issue_class] > 0][
            [SubmissionColumns.STEP_ID.value]].value_counts().to_csv(issue_stats_path)


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    parser = argparse.ArgumentParser()

    parser.add_argument('submissions_path', type=str,
                        help='Path to .csv file with preprocessed submissions with series')
    parser.add_argument('issues_statistics_path', type=str,
                        help='Path to .csv file with submissions issues count statistics')
    parser.add_argument('issues_info_path', type=str, help='Path to .csv file with issues list (classes and types)')
    parser.add_argument('issues_steps_statistics_directory_path', type=str,
                        help='Path to directory where to save issues steps statistics for each issue class')
    parser.add_argument('--attempt-number', type=Optional[int], default=None,
                        help='Number of attempt to analyze (None --all, 1 -- first, -1 --last, and other)')

    args = parser.parse_args(sys.argv[1:])
    configure_logger(args.issues_steps_statistics_directory_path, 'statistics')

    get_issues_steps_statistics(args.submissions_path,
                                args.issues_statistics_path,
                                args.issues_steps_statistics_directory_path,
                                args.issues_info_path,
                                args.attempt_number)
