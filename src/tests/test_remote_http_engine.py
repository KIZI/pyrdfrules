import unittest
from unittest.mock import patch, MagicMock
from pyrdfrules.config import Config
from pyrdfrules.engine.remote_http_engine import RemoteHttpEngine
from pyrdfrules.common.http.url import Url

class TestRemoteHttpEngine(unittest.TestCase):

    @patch('pyrdfrules.engine.remote_http_engine.HTTPRDFRulesApi')
    def test_start(self, MockHTTPRDFRulesApi):
        mock_api = MagicMock()
        MockHTTPRDFRulesApi.return_value = mock_api

        engine = RemoteHttpEngine(url="http://example.com", config=Config())
        engine.start()
        engine.check()
        mock_api.workspace.get_all_files.assert_called_once()

    @patch('pyrdfrules.engine.remote_http_engine.HTTPRDFRulesApi')
    def test_stop(self, MockHTTPRDFRulesApi):
        mock_api = MagicMock()
        MockHTTPRDFRulesApi.return_value = mock_api

        engine = RemoteHttpEngine(url="http://example.com", config=Config())
        engine.start()
        engine.stop()

        mock_api.workspace.get_all_files.assert_not_called()
        mock_api.workspace.assert_not_called()

if __name__ == '__main__':
    unittest.main()
