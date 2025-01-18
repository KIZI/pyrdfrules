import time
import unittest
from unittest.mock import patch, MagicMock
import pyrdfrules
from pyrdfrules.application import Application
from pyrdfrules.config import Config

class TestLocalApplication(unittest.TestCase):
    
    def test_runs_local(self):
        """
        Check if the application runs locally, does not crash and terminates correctly.
        """
        
        app = pyrdfrules.application.Application()
        rdfrules = app.start_local(
            install_jvm = True,
            install_rdfrules = True
        )
        self.assertIsNotNone(rdfrules, "Should not be None")
        time.sleep(10)
        app.stop()
        
    def test_runs_workspace(self):
        """
        Check if the application runs with a workspace, does not crash and terminates correctly.
        """
        
        app = pyrdfrules.application.Application()
        
        rdfrules = app.start_local(
            install_jvm = True,
            install_rdfrules = True
        )
        
        self.assertIsNotNone(rdfrules, "Should not be None")
        rdfrules.engine.check()
        
        app.stop()

if __name__ == '__main__':
    unittest.main()
