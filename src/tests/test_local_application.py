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

class TestApplication(unittest.TestCase):

    @patch('pyrdfrules.application.RDFRules')
    def test_start_local(self, MockRDFRules):
        mock_engine = MagicMock()
        MockRDFRules.return_value.engine = mock_engine

        app = Application()
        rdfrules = app.start_local(install_jvm=True, install_rdfrules=True)

        self.assertIsNotNone(rdfrules)
        mock_engine.start.assert_called_once()

    @patch('pyrdfrules.application.RemoteHttpEngine')
    def test_start_remote(self, MockRDFRules):
        mock_engine = MagicMock()
        MockRDFRules.return_value = mock_engine

        app = Application()
        rdfrules = app.start_remote(url="http://example.com", config=Config())

        self.assertIsNotNone(rdfrules)
        mock_engine.start.assert_called_once()

    @patch('pyrdfrules.application.RDFRules')
    def test_stop(self, MockRDFRules):
        mock_engine = MagicMock()
        MockRDFRules.return_value.engine = mock_engine

        app = Application()
        app.start_local(install_jvm=True, install_rdfrules=True)
        app.stop()

        mock_engine.stop.assert_called_once()

if __name__ == '__main__':
    unittest.main()
