"""
[
  {
    "name": "LoadGraph",
    "parameters": {
      "path": "/data/wn18rr/train.tsv",
      "settings": "tsvParsedUris"
    }
  },
  {
    "name": "Histogram",
    "parameters": {
      "subject": true,
      "predicate": false,
      "object": false
    }
  }
]
"""

import time
import unittest

from pyrdfrules.common.http.url import Url

import pyrdfrules.application
from pyrdfrules.common.result.histogram import HistogramResult, HistogramSingleResult
from pyrdfrules.common.task.task import Task
from pyrdfrules.config import Config
import os


import os
import time
import unittest
from unittest.mock import patch, MagicMock

import requests
import pyrdfrules
from pyrdfrules.application import Application
from pyrdfrules.common.result.result import Result
from pyrdfrules.config import Config
from pyrdfrules.config import Config
from pyrdfrules.rdfrules.commondata import ConfidenceType, Constraint, RuleConsumer, RuleConsumerType, Threshold
from pyrdfrules.rdfrules.jsonformats import PrefixFull
from pyrdfrules.rdfrules.pipeline import ComputeConfidence, GetRules, GraphAwareRules, Histogram, Index, LoadGraph, MergeDatasets, AddPrefixes, Mine, Pipeline, SortRuleset

def get_path(file_name):
    return os.path.join(os.path.dirname((os.path.realpath(__file__))), "data", file_name)

# slightly modified from
# from https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
def download_file(url, file_name, base_path):
    file_path = os.path.join(base_path, "dbpedia_yago", file_name)
    
    os.makedirs(os.path.join(base_path, "dbpedia_yago"), exist_ok=True)
    
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

class TestHistogram(unittest.TestCase):
    
    def setUp(self):
        # download the pipeline files
        self.config = Config(
            workspace_path=os.path.realpath(os.path.join(os.path.dirname((os.path.realpath(__file__))), "..", "rdfrules", "workspace"))
        )
        
        download_file("http://rdfrules.vse.cz/api/workspace/dbpedia_yago/mappingbased_objects_sample.ttl", "mappingbased_objects_sample.ttl", self.config.workspace_path)

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
    
    def test_histogram(self):
        """
        Runs a pipeline locally.
        """

        pipeline = Pipeline(
            tasks=[
                LoadGraph(
                    graphName = "<dbpedia>",
                    path = "/dbpedia_yago/mappingbased_objects_sample.ttl"
                ),
                Histogram(
                    subject=True,
                )
            ]
        )
        
        task = self.rdfrules.task.create_task(pipeline)
            
        for step in self.rdfrules.task.run_task(task):
            print(step)
            self.assertIsNotNone(step, "Should not be None")
            self.assertIsInstance(step, Task, "Should be an instance of Task")
        
        self.assertIsNotNone(task.result, "Should not be None")
        self.assertTrue(task.finished, "Should be finished")
        
        print(task.result)
        
        histogram = task.get_result().get_histogram()
        
        self.assertIsInstance(histogram, HistogramResult)
        self.assertTrue(len(histogram.list) > 0)
        
        for item in histogram.list:
            self.assertIsInstance(item, HistogramSingleResult)
            
        top_ten_items = histogram.get_top(10)
        
        self.assertTrue(len(top_ten_items) == 10)
        
        print(top_ten_items)
        
        histogram.print(top_n=10)
        
        #for eval in task.get_result().get_evaluations():
        #    print(eval)
        #    eval.print()
        #
        #self.assertIsNotNone(task.result, "Should not be None")
        #self.assertIsInstance(task.result, list, "Should be a list")
        #
        #self.assertIsNotNone(task.get_result(), "Should not be None")
        #self.assertIsInstance(task.get_result(), Result, "Should be a Result")

if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
