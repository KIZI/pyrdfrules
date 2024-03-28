from pydantic import BaseModel

class Graph(BaseModel):
    
    """
    Graph name: Name for this loaded graph. It must have the URI notation in angle brackets, e.g., or <http://dbpedia.org>.
    """
    name: str