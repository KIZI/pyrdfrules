from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext


class CacheApi():
    
    context: RDFRulesApiContext
    
    def __init__(self, context: RDFRulesApiContext) -> None:
        self.context = context
        pass
    
    def get_memory_info(self):
        """Gets memory info.
        """
        
    def clear(self):
        """Clears the cache.
        """
    
    def delete(self, key: str):
        """Deletes a key from the cache.
        """
        
    def alias(self, key: str, alias: str):
        """Creates an alias for a key.
        """