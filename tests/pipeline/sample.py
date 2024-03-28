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
from pyrdfrules.pipeline.sort.sort import AddPrefixes, Sort
from pyrdfrules.pipeline.transformation.merge_datasets import MergeDatasets


pipeline = Pipeline(
    items=[
        LoadGraph(
            file="mappingbased_objects_sample.ttl",
            graph_name='<dbpedia>'
        ),
        LoadGraph(
            file="yagoFacts.tsv",
            graph_name='<yago>'
        ),
        LoadGraph(
            file="yagoDBpediaInstances.tsv",
            graph_name='<dbpedia>'
        ),
        MergeDatasets(),
        AddPrefixes(
            sort_by=[
                # todo
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