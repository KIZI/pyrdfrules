from pyrdfrules.api.cache.cache_api import CacheApi
from pyrdfrules.api.http_api_urls import CACHE_CLEAR_URL, CACHE_MEMORY_URL, CACHE_DELETE_URL
from pyrdfrules.api.http_rdfrules_api_context import HTTPRDFRulesApiContext


class CacheHttpApi(CacheApi):
    
    __doc__ = CacheApi.__doc__
    
    def __init__(self, context: HTTPRDFRulesApiContext) -> None:
        super().__init__(context)
        pass
    
    def get_memory_info(self) -> dict:
        return self.context.get_http_client().get(CACHE_MEMORY_URL).json()
    
    def clear(self) -> None:
        self.context.get_http_client().get(CACHE_CLEAR_URL)
    
    def delete(self, key: str) -> None:
        self.context.get_http_client().delete(CACHE_DELETE_URL.format(key = key))
    
    def alias(self, key: str, alias: str) -> None:
        pass