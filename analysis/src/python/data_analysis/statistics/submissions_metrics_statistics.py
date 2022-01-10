import argparse
import logging
import sys

from analysis.src.python.data_analysis.model.column_name import SubmissionColumns, SubmissionColumnsStats
from analysis.src.python.data_analysis.utils.df_utils import read_df, write_df
from analysis.src.python.data_analysis.utils.stats_utils import calculate_code_lines_count, \
    calculate_code_symbols_count, calculate_issues_count


def get_submission_statistics(submissions_with_issues_path: str, submissions_statistics_path: str):
    """ Calculate submissions metrics such number of code lines, symbols, issues. """

    df_submissions = read_df(submissions_with_issues_path)
    df_stats = df_submissions[[SubmissionColumns.ID]].copy()

    df_stats[SubmissionColumnsStats.CODE_LINES_COUNT.value] = df_submissions[SubmissionColumns.CODE.value] \
        .apply(calculate_code_lines_count)
    df_stats[SubmissionColumnsStats.CODE_SYMBOLS_COUNT.value] = df_submissions[SubmissionColumns.CODE.value] \
        .apply(calculate_code_symbols_count)

    df_stats[SubmissionColumnsStats.QODANA_ISSUE_COUNT.value] = df_submissions[SubmissionColumns.QODANA_ISSUES.value] \
        .apply(calculate_issues_count)
    df_stats[SubmissionColumnsStats.RAW_ISSUE_COUNT.value] = df_submissions[SubmissionColumns.RAW_ISSUES.value] \
        .apply(calculate_issues_count)

    write_df(df_stats, submissions_statistics_path)


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    parser = argparse.ArgumentParser()

    parser.add_argument('submissions_path', type=str,
                        help='Path to .csv file with preprocessed submissions with issues')
    parser.add_argument('submissions_statistics_path', type=str,
                        help='Path to .csv file where to save submissions statistics')
    args = parser.parse_args(sys.argv[1:])

    get_submission_statistics(args.submissions_path, args.submissions_statistics_path)
