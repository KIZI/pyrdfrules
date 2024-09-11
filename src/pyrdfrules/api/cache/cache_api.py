from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext


class CacheApi():
    
    context: RDFRulesApiContext
    
    def __init__(self, context: RDFRulesApiContext) -> None:
        self.context = context
        pass
    
    async def get_memory_info():
        """Gets memory info.
        """
        
    async def clear():
        """Clears the cache.
        """
    
    async def delete(key: str):
        """Deletes a key from the cache.
        """
        
    async def alias(key: str, alias: str):
        """Creates an alias for a key.
        """