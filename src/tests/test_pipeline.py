import logging
import os
import time
import unittest

from pyrdfrules.common.http.url import Url

import pyrdfrules.application
from pyrdfrules.common.task.task import Task
from pyrdfrules.config import Config
from pyrdfrules.rdfrules.commondata import ConfidenceType, Threshold
from pyrdfrules.rdfrules.jsonformats import PrefixFull
from pyrdfrules.rdfrules.pipeline import ComputeConfidence, GetRules, GraphAwareRules, Index, LoadGraph, MergeDatasets, AddPrefixes, Mine, SortRuleset

class TestPipeline(unittest.TestCase):
        
    def test_runs_workspace(self):
        """
        Check if the application runs with a workspace, does not crash and terminates correctly.
        """
        
        app = pyrdfrules.application.Application()
        
        rdfrules = app.start_remote(
            url = Url("http://rdfrules.vse.cz/api/")
        )
        
        self.assertIsNotNone(rdfrules, "Should not be None")
        rdfrules.workspace.get_files()
        

        print(LoadGraph(
            graphName = "<dbpedia>",
            path = "/dbpedia_yago/mappingbased_objects_sample.ttl"
        ).json())
        
        print(MergeDatasets().json())
        
        print(AddPrefixes(prefixes=[PrefixFull(prefix="dbpedia", nameSpace="http://dbpedia.org/resource/")]).json())
        
        print(Index(train=[], test=[]).json())
        
        print(Mine(thresholds=[Threshold(name="Timeout", value=0.5)]).json())
        
        print(ComputeConfidence(confidenceType=ConfidenceType.PCA_CONFIDENCE, min=0.5, topk=50).json())
        
        print(SortRuleset(by=[]).json())
        
        print(GraphAwareRules().json())
        
        print(GetRules().json())
        
        
        
        app.stop()


if __name__ == '__main__':
    unittest.main()
