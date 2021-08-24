import pytest
from hyperstyle.src.python import MAIN_FOLDER
from analysis.test.python.evaluation import XLSX_DATA_FOLDER
from analysis.test.python.evaluation.testing_config import get_testing_arguments
from evaluation.evaluation_config import EvaluationConfig
from evaluation.evaluation_run_tool import get_solutions_df, inspect_solutions_df


def test_correct_tool_path():
    try:
        testing_arguments_dict = get_testing_arguments(to_add_traceback=True, to_add_tool_path=True)
        testing_arguments_dict.solutions_file_path = XLSX_DATA_FOLDER / 'test_unsorted_order.xlsx'
        config = EvaluationConfig(testing_arguments_dict)
        lang_code_dataframe = get_solutions_df(config.extension, config.solutions_file_path)
        inspect_solutions_df(config, lang_code_dataframe)
    except Exception:
        pytest.fail("Unexpected error")


def test_incorrect_tool_path():
    with pytest.raises(Exception):
        testing_arguments_dict = get_testing_arguments(to_add_traceback=True)
        testing_arguments_dict.solutions_file_path = XLSX_DATA_FOLDER / 'test_unsorted_order.xlsx'
        testing_arguments_dict.tool_path = MAIN_FOLDER.parent / 'review/incorrect_path.py'
        config = EvaluationConfig(testing_arguments_dict)
        lang_code_dataframe = get_solutions_df(config.extension, config.solutions_file_path)
        assert inspect_solutions_df(config, lang_code_dataframe)
