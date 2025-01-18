import os
import time
import unittest
from unittest.mock import patch, MagicMock

import requests
import pyrdfrules
from pyrdfrules.application import Application
from pyrdfrules.config import Config
from pyrdfrules.config import Config


class TestMultipleLocalInstances(unittest.TestCase):
    
    def setUp(self):
        # download the pipeline files
        self.config = Config(
            workspace_path=os.path.realpath(os.path.join(os.path.dirname((os.path.realpath(__file__))), "..", "rdfrules", "workspace"))
        )

        self.instance = pyrdfrules.application.Application()

        return super().setUp()
    
    def tearDown(self):
        self.instance.stop()
        return super().tearDown()
    
    def test_starts_multiple(self):
        """
        Runs multiple instances locally.
        """

        rdfrules_one = self.instance.start_local(
            install_jvm = True,
            install_rdfrules = True,
            config = self.config,
            port = 8851
        )
        
        rdfrules_two = self.instance.start_local(
            install_jvm = True,
            install_rdfrules = True,
            config = self.config,
            port = 8852
        )
        
        rdfrules_three = self.instance.start_local(
            install_jvm = True,
            install_rdfrules = True,
            config = self.config
        )
        
        self.assertIsNotNone(rdfrules_one)
        self.assertIsNotNone(rdfrules_two)
        self.assertIsNotNone(rdfrules_three)
        
        # should not throw
        rdfrules_one.engine.check()
        rdfrules_two.engine.check()
        rdfrules_three.engine.check()
        

if __name__ == '__main__':
    unittest.main()
