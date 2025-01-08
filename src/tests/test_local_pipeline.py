import os
import time
import unittest
from unittest.mock import patch, MagicMock

import requests
import pyrdfrules
from pyrdfrules.application import Application
from pyrdfrules.config import Config
from pyrdfrules.config import Config
from pyrdfrules.rdfrules.commondata import ConfidenceType, Constraint, RuleConsumer, RuleConsumerType, Threshold
from pyrdfrules.rdfrules.jsonformats import PrefixFull
from pyrdfrules.rdfrules.pipeline import ComputeConfidence, GetRules, GraphAwareRules, Index, LoadGraph, MergeDatasets, AddPrefixes, Mine, Pipeline, SortRuleset

def get_path(file_name):
    return os.path.join(os.path.dirname((os.path.realpath(__file__))), "data", file_name)

# slightly modified from
# from https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
def download_file(url, file_name, base_path):
    file_path = os.path.join(base_path, "dbpedia_yago", file_name)
    print(file_path)
    # check if the file already exists
    if os.path.exists(file_path):
        return
    
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)

class TestLocalPipeline(unittest.TestCase):
    
    def setUp(self):
        # download the pipeline files
        self.config = Config(
            workspace_path=os.path.realpath(os.path.join(os.path.dirname((os.path.realpath(__file__))), "..", "rdfrules", "workspace"))
        )
        
        download_file("http://rdfrules.vse.cz/api/workspace/dbpedia_yago/mappingbased_objects_sample.ttl", "mappingbased_objects_sample.ttl", self.config.workspace_path)
        download_file("http://rdfrules.vse.cz/api/workspace/dbpedia_yago/yagoFacts.tsv", "yagoFacts.tsv", self.config.workspace_path)
        download_file("http://rdfrules.vse.cz/api/workspace/dbpedia_yago/yagoDBpediaInstances.tsv", "yagoDBpediaInstances.tsv", self.config.workspace_path)

        self.instance = app = pyrdfrules.application.Application()
        
        self.rdfrules = app.start_local(
            install_jvm = True,
            install_rdfrules = True,
            config = self.config
        )

        return super().setUp()
    
    def tearDown(self):
        self.instance.stop()
        return super().tearDown()
    
    def test_runs_local(self):
        """
        Runs a pipeline locally.
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
        
        task = self.rdfrules.task.create_task(pipeline)
            
        for step in self.rdfrules.task.run_task(task):
            print(step)
            self.assertIsNotNone(step, "Should not be None")
        
        print(task.result)

if __name__ == '__main__':
    unittest.main()
