from os import path

from pyrdfrules.common.http.url import Url
from pyrdfrules.common.file.workspace import Workspace
from pyrdfrules.common.graph.remote_graph import RemoteGraph
from pyrdfrules.common.graph.workspace_graph import WorkspaceGraph
from pyrdfrules.pipeline.index.confidence import ComputeConfidence
from pyrdfrules.pipeline.index.confidencemetric.pca_confidence import PCAConfidence
from pyrdfrules.pipeline.index.index import Index
from pyrdfrules.pipeline.index.mine_rules import MineRules
from pyrdfrules.pipeline.index.ruleconsumer.on_disk import OnDisk
from pyrdfrules.pipeline.index.ruleconsumer.top_k import TopK
from pyrdfrules.pipeline.index.thresholds.max_rule_length import MaxRuleLength
from pyrdfrules.pipeline.index.thresholds.min_head_coverage import MinHeadCoverage
from pyrdfrules.pipeline.index.thresholds.min_head_size import MinHeadSize
from pyrdfrules.pipeline.index.thresholds.timeout import Timeout
from pyrdfrules.pipeline.load.load_graph import LoadGraph
from pyrdfrules.pipeline.pipeline import Pipeline
from pyrdfrules.pipeline.ruleset.get_rules import GetRules
from pyrdfrules.pipeline.ruleset.to_graph_aware_rules import ToGraphAwareRules
from pyrdfrules.pipeline.sort.measure.cluster import Cluster
from pyrdfrules.pipeline.sort.sort import Sort
from pyrdfrules.pipeline.transformation.add_prefixes import AddPrefixes
from pyrdfrules.pipeline.transformation.merge_datasets import MergeDatasets
from pyrdfrules.rdfrules.rdfrules import RDFRules

workspace = Workspace(
    path.abspath("./workspace")
)

yago = workspace.open('yagoFacts.tsv')
yago_dbpedia = workspace.open('yagoDBpediaInstances.tsv')

dbpedia_graph = WorkspaceGraph("<dbpedia>", workspace.open('mappingbased_objects_sample.ttl'))

# sample
graph_remote = RemoteGraph("<wikidata>", Url("https://graph"))

pipeline = Pipeline(
    items=[
        LoadGraph(
            graph=dbpedia_graph
        ),
        LoadGraph(
            file=yago,
            graph_name='<yago>'
        ),
        LoadGraph(
            file=yago_dbpedia,
            graph_name='<dbpedia>'
        ),
        MergeDatasets(),
        AddPrefixes(
            sort_by=[
                # ...
            ]
        ),
        Index(),
        MineRules(
            thresholds=[
                MinHeadSize(100),
                MaxRuleLength(3),
                Timeout(5),
                MinHeadCoverage(0.01)
            ],
            rule_consumer=[
                TopK(
                    1000,
                    allow_overflow=False
                ),
                OnDisk(
                    export_path="out",
                    export_format="ndjson"
                )
            ]
        ),
        ComputeConfidence(
            PCAConfidence(
                0.5,
                top_k=50
            )
        ),
        Sort([Cluster()]),
        ToGraphAwareRules(),
        GetRules()
    ]
)

rdfrules = RDFRules(
    workspace=workspace
)

# needs to be in an function, here just for showcase
ruleset = rdfrules.launch(pipeline)

for rule in ruleset:
    print(rule.head)
    print(rule.body)
    
    for measure in rule.measures:
        print(measure)
        
        
# logs ? we want to see some output while it's running
# is blocking, add option for generator