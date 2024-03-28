from typing import Optional

from pydantic_core import Url
from pyrdfrules.common.file.workspace_file import WorkspaceFile
from pyrdfrules.common.graph.graph import Graph
from pyrdfrules.pipeline.pipeline_item import PipelineItem

class LoadGraph(PipelineItem):
    """
    Load graph (set of triples) from a file in the workspace or from a remote file available via URL. The source is in some RDF or relational SQL format and is supposed as a single graph.
    """
    
    """
    File from the current workspace containing the graph data. The dataset format is detected automatically by the file extension. Supported extensions are .ttl (turtle), .nt (n-triples), .nq (n-quads), .json | .jsonld (JSON-LD), .xml | .rdf | .owl (RDF/XML), .trig (TriG), .trix (TriX), .tsv, .sql, .cache (internal binary format). All formats can be compressed by GZIP or BZ2 (e.g. data.ttl.gz).
    """
    file: Optional[WorkspaceFile]
    
    """
    URL: A URL to a remote file to be loaded. If this is specified then the workspace file is ommited.
    """
    url: Optional[Url]
    
    """
    Graph name: Name for this loaded graph. It must have the URI notation in angle brackets, e.g., or <http://dbpedia.org>.
    """
    graph_name: Optional[str]
    
    """
    Graph object to be loaded.
    """
    graph: Optional[Graph]