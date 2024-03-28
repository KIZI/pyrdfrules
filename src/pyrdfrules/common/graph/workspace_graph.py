from pydantic import BaseModel
from pydantic_core import Url

from pyrdfrules.common.file.workspace_file import WorkspaceFile
from pyrdfrules.common.graph.graph import Graph

class WorkspaceGraph(Graph):
    
    """
    File from the current workspace containing the graph data.
    The dataset format is detected automatically by the file extension.
    Supported extensions are .ttl (turtle), .nt (n-triples), .nq (n-quads), .json | .jsonld (JSON-LD), .xml | .rdf | .owl (RDF/XML), .trig (TriG), .trix (TriX), .tsv, .sql, .cache (internal binary format).
    All formats can be compressed by GZIP or BZ2 (e.g. data.ttl.gz).
    """
    file: WorkspaceFile
    
    """
    Graph name: Name for this loaded graph. It must have the URI notation in angle brackets, e.g., or <http://dbpedia.org>.
    """
    name: str