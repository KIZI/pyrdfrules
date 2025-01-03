import json
import logging
import os
import time
import unittest

from pyrdfrules.common.http.url import Url

import pyrdfrules.application
from pyrdfrules.common.task.task import Task
from pyrdfrules.config import Config
from pyrdfrules.rdfrules.commondata import ConfidenceType, Constraint, RuleConsumer, RuleConsumerType, Threshold
from pyrdfrules.rdfrules.jsonformats import PrefixFull
from pyrdfrules.rdfrules.pipeline import ComputeConfidence, GetRules, GraphAwareRules, Index, LoadGraph, MergeDatasets, AddPrefixes, Mine, Pipeline, SortRuleset

class TestPipeline(unittest.TestCase):
        
    def test_pipeline_matches(self):
        """
        Check if test pipeline matches the pipeline from the file.
        """

        pipeline = Pipeline(
            tasks=[
                LoadGraph(
                    graphName = "<dbpedia>",
                    path = "/dbpedia_yago/mappingbased_objects_sample.ttl"
                ),
                LoadGraph(
                    graphName = "<yago>",
                    path = "/dbpedia_yago/yagoFacts.tsv",
                    settings = "tsvParsedUris"
                ),
                LoadGraph(
                    graphName = "<dbpedia>",
                    path = "/dbpedia_yago/yagoDBpediaInstances.tsv",
                    settings = "tsvParsedUris"
                ),
                MergeDatasets(),
                AddPrefixes(
                    prefixes=[
                        PrefixFull(prefix="dbo", nameSpace="http://dbpedia.org/ontology/"),
                        PrefixFull(prefix="dbr", nameSpace="http://dbpedia.org/resource/")
                    ]
                ),
                Index(train=[], test=[]),
                Mine(
                    thresholds=[
                        Threshold(name="MinHeadSize", value=100),
                        Threshold(name="MaxRuleLength", value=3),
                        Threshold(name="Timeout", value=5),
                        Threshold(name="MinHeadCoverage", value=0.01),
                    ],
                    ruleConsumers=[
                        RuleConsumer(
                            name=RuleConsumerType.TOP_K,
                            k=1000,
                            allowOverflow=False
                        )
                    ],
                    patterns=[],
                    constraints=[
                        Constraint(name="WithoutConstants")
                    ],
                    parallelism=0
                ),
                ComputeConfidence(confidenceType=ConfidenceType.PCA_CONFIDENCE, min=0.5, topk=50),
                SortRuleset(by=[]),
                GraphAwareRules(),
                GetRules()
            ]
        )
        
        path = os.path.join(os.getcwd(), "src/tests/data/task.json")
        
        with open(path, "r") as file:        
            task_json_from_file = json.loads(file.read())
            
            
            a, b = json.dumps(task_json_from_file, sort_keys=True), json.dumps(pipeline.model_dump(), sort_keys=True)
            
            self.assertEqual(a, b)
        return
    

    def test_pipeline_execution(self):
        """
        Tests if the application can run the pipeline.
        """
        
        app = pyrdfrules.application.Application()
        
        rdfrules = app.start_remote(
            url = Url("http://rdfrules.vse.cz/api/"),
            config=Config(
                task_update_interval_ms=1000
            )
        )
        
        self.assertIsNotNone(rdfrules, "Should not be None")
        
        pipeline = Pipeline(
            tasks=[
                LoadGraph(
                    graphName = "<dbpedia>",
                    path = "/dbpedia_yago/mappingbased_objects_sample.ttl"
                ),
                LoadGraph(
                    graphName = "<yago>",
                    path = "/dbpedia_yago/yagoFacts.tsv",
                    settings = "tsvParsedUris"
                ),
                LoadGraph(
                    graphName = "<dbpedia>",
                    path = "/dbpedia_yago/yagoDBpediaInstances.tsv",
                    settings = "tsvParsedUris"
                ),
                MergeDatasets(),
                AddPrefixes(
                    prefixes=[
                        PrefixFull(prefix="dbo", nameSpace="http://dbpedia.org/ontology/"),
                        PrefixFull(prefix="dbr", nameSpace="http://dbpedia.org/resource/")
                    ]
                ),
                Index(train=[], test=[]),
                Mine(
                    thresholds=[
                        Threshold(name="MinHeadSize", value=100),
                        Threshold(name="MaxRuleLength", value=3),
                        Threshold(name="Timeout", value=5),
                        Threshold(name="MinHeadCoverage", value=0.01),
                    ],
                    ruleConsumers=[
                        RuleConsumer(
                            name=RuleConsumerType.TOP_K,
                            k=1000,
                            allowOverflow=False
                        )
                    ],
                    patterns=[],
                    constraints=[
                        Constraint(name="WithoutConstants")
                    ],
                    parallelism=0
                ),
                ComputeConfidence(confidenceType=ConfidenceType.PCA_CONFIDENCE, min=0.5, topk=50),
                SortRuleset(by=[]),
                GraphAwareRules(),
                GetRules()
            ]
        )
        
        task : Task = None
        
        task = rdfrules.task.create_task(pipeline)
            
        for step in rdfrules.task.run_task(task):
            print(step)
            self.assertIsNotNone(step, "Should not be None")
        
        print(task.result)
        
        app.stop()

if __name__ == '__main__':
    unittest.main()
