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

class TestAplicationSetup(unittest.TestCase):
    
    def _create_application(self, **kwargs):
        app = pyrdfrules.application.Application()
        
        config = Config(
            workspace_path=os.path.realpath(os.path.join(os.path.dirname((os.path.realpath(__file__))), "..", "rdfrules", "workspace"))
        )
        
        app.start_local(**kwargs, config = config)
        return app
    
    def test_base_creation(self):
        """
        Tests installation of JVM and RDFRules with no parameters.
        """
        
        app = self._create_application(install_jvm=True, install_rdfrules=True)
        self.assertIsNotNone(app)
        app.stop()
        
    def test_rdfrules_custom_install_path(self):
        """
        Tests installation of JVM and RDFRules with workspace.
        """
        
        app = self._create_application(
            install_jvm=True,
            install_rdfrules=True,
            rdfrules_path=os.path.realpath(os.path.join(os.path.dirname((os.path.realpath(__file__))), "..", "rdfrules")),    
        )
        
        self.assertIsNotNone(app)
        app.stop()

    def test_rdfrules_custom_jvm_install_path(self):
        """
        Tests installation of JVM and RDFRules with workspace.
        """
        
        app = self._create_application(
            install_jvm=True,
            install_rdfrules=True,
            jvm_path=os.path.realpath(os.path.join(os.path.dirname((os.path.realpath(__file__))), "..", "jvm")),
            rdfrules_path=os.path.realpath(os.path.join(os.path.dirname((os.path.realpath(__file__))), "..", "rdfrules")),    
        )
        
        self.assertIsNotNone(app)
        app.stop()

if __name__ == '__main__':
    unittest.main()
