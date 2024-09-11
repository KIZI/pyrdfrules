from pyrdfrules.api.cache.cache_api import CacheApi
from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext
from pyrdfrules.api.task.task_api import TaskApi
from pyrdfrules.api.workspace.workspace_api import WorkspaceApi


class RDFRulesApi():
    cache: CacheApi
    workspace: WorkspaceApi
    task: TaskApi
    context: RDFRulesApiContext
    
    def __init__(self, context: RDFRulesApiContext) -> None:
        self.context = context
        pass