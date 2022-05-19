import ast
import json
from datetime import datetime
from typing import Dict, List

from hyperstyle.src.python.review.inspectors.issue import BaseIssue

from analysis.src.python.evaluation.issues_statistics.common.raw_issue_encoder_decoder import RawIssueDecoder
from analysis.src.python.evaluation.qodana.util.models import QodanaIssue


def str_to_dict(s: str) -> Dict:
    """ Load dict from string. """

    return json.loads(s)


def dict_to_str(d: Dict) -> str:
    """ Dump dict to string. """

    return json.dumps(d)


def list_to_str(ls: List) -> str:
    """ Dump dict to string. """

    return json.dumps(ls)


def str_to_datetime(s) -> datetime:
    """ Parse datetime from string. """

    return datetime.fromisoformat(s)


def parse_qodana_issues(s: str) -> str:
    """ Parse qodana issues from string and . """

    return list_to_str(list(map(ast.literal_eval, ast.literal_eval(s)['issues'])))


def parse_qodana_issues_to_objects(s: str) -> List[QodanaIssue]:
    return list(map(lambda issue: QodanaIssue.from_json(json.dumps(issue)), ast.literal_eval(s)))


def parse_raw_issues_to_objects(s: str) -> List[BaseIssue]:
    return json.loads(s, cls=RawIssueDecoder)


def dump_qodana_issues_to_str(issues: List[QodanaIssue]) -> str:
    return list_to_str(list(map(lambda issue: QodanaIssue.to_json(issue), issues)))
