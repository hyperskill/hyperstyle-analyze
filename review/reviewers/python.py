from pathlib import Path
from typing import List

from review.application_config import ApplicationConfig
from review.common.file_system import get_all_subdirs
from review.common.language import Language
from review.reviewers.common import perform_language_review
from review.reviewers.review_result import ReviewResult
from review.reviewers.utils.metadata_exploration import Metadata, ProjectMetadata


def perform_python_review(metadata: Metadata, config: ApplicationConfig) -> ReviewResult:
    created_file_paths = []
    if isinstance(metadata, ProjectMetadata):
        created_file_paths.extend(create_init_scripts_in_subdirs(metadata.path))

    review_result = perform_language_review(metadata, config, Language.PYTHON)
    review_result.file_review_results = [
        file_review_result for file_review_result in review_result.file_review_results
        if file_review_result.file_path not in created_file_paths
    ]
    return review_result


def create_init_scripts_in_subdirs(path: Path) -> List[Path]:
    created_file_paths = []
    for subdir in get_all_subdirs(path):
        init_file_path = subdir / '__init__.py'
        if not init_file_path.is_file():
            init_file_path.touch()
            created_file_paths.append(init_file_path)

    return created_file_paths
