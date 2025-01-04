from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext


class CacheApi():
    
    context: RDFRulesApiContext
    
    def __init__(self, context: RDFRulesApiContext) -> None:
        self.context = context
        pass
    
    def get_memory_info(self) -> dict:
        """Gets memory info.
        
        Returns:
            dict: Memory info.
        
        """
        
    def clear(self) -> None:
        """Clears the cache.
        
        Returns:
            None
        """
    
    def delete(self, key: str) -> None:
        """Deletes a key from the cache.
        
        Args:
            key (str): Key to delete.
            
        Throws:
            Exception: If the key does not exist.
        """
        
    def alias(self, key: str, alias: str):
        """Creates an alias for a key.
        
        Args:
            key (str): Key to alias.
            alias (str): Alias to create.
            
        Throws:
            Exception: If the key does not exist.
        """