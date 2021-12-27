from dataclasses import dataclass, field
from typing import List, Optional, Dict

from data.common_api.response import PageRequestParams, PageResponse, Object


@dataclass
class ProjectsRequestParams(PageRequestParams):
    pass


@dataclass
class ProjectsByLevel:
    easy: List[int] = field(default_factory=list)
    medium: List[int] = field(default_factory=list)
    hard: List[int] = field(default_factory=list)
    nightmare: List[int] = field(default_factory=list)


@dataclass
class Project(Object):
    id: int
    title: str
    use_ide: bool
    environment: str
    description: str
    is_beta: bool
    is_template_based: bool
    results: str
    stages_count: int
    n_first_prerequisites: int
    n_last_prerequisites: int
    language: str
    is_deprecated: bool
    progress_id: str
    readiness: int
    lesson_stepik_id: Optional[int]
    preview_step: Optional[int] = None
    ide_files: Optional[str] = None
    stages_ids: List[int] = field(default_factory=list)
    url: str = field(init=False)
    tracks: Dict[str, Dict[str, str]] = field(default_factory=dict)

    def __post_init__(self):
        self.url = f'https://hyperskill.org/projects/{self.id}'


@dataclass
class ProjectsResponse(PageResponse[Project]):
    projects: List[Project]

    def get_objects(self) -> List[Project]:
        return self.projects
