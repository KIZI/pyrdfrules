import unittest
from unittest.mock import patch, MagicMock
from requests import Response
from pyrdfrules.common.http.http_client import HttpClient
from pyrdfrules.config import Config

class TestHttpClient(unittest.TestCase):

    def setUp(self):
        self.config = Config()
        self.client = HttpClient(config=self.config)
        self.client.set_base_url("http://example.com")

    @patch('pyrdfrules.common.http.http_client.Session.get')
    def test_get(self, mock_get):
        mock_response = MagicMock(spec=Response)
        mock_get.return_value = mock_response

        response = self.client.get("/test")

        mock_get.assert_called_once_with("http://example.com/test")
        self.assertEqual(response, mock_response)

    @patch('pyrdfrules.common.http.http_client.Session.post')
    def test_post(self, mock_post):
        mock_response = MagicMock(spec=Response)
        mock_post.return_value = mock_response

        response = self.client.post("/test", json={"key": "value"})

        mock_post.assert_called_once_with("http://example.com/test", json={"key": "value"})
        self.assertEqual(response, mock_response)

    @patch('pyrdfrules.common.http.http_client.Session.delete')
    def test_delete(self, mock_delete):
        mock_response = MagicMock(spec=Response)
        mock_delete.return_value = mock_response

        response = self.client.delete("/test")

        mock_delete.assert_called_once_with("http://example.com/test")
        self.assertEqual(response, mock_response)

if __name__ == '__main__':
    unittest.main()
