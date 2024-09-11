from pyrdfrules.api.rdfrules_api import RDFRulesApi
from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext


class HTTPRDFRulesApi(RDFRulesApi):

    def __init__(self, context: RDFRulesApiContext) -> None:
        super().__init__(context)
        self.cache = None
        self.workspace = None
        self.task = None
        pass