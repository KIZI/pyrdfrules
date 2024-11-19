from pyrdfrules.api.cache.cache_http_api import CacheHttpApi
from pyrdfrules.api.rdfrules_api import RDFRulesApi
from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext
from pyrdfrules.api.task.task_http_api import TaskHttpApi
from pyrdfrules.api.workspace.workspace_http_api import WorkspaceHttpApi


class HTTPRDFRulesApi(RDFRulesApi):

    def __init__(self, context: RDFRulesApiContext) -> None:
        super().__init__(context)
        self.cache = CacheHttpApi(context)
        self.workspace = WorkspaceHttpApi(context)
        self.task = TaskHttpApi(context)
        pass