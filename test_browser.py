import unittest
from unittest.mock import patch
from browser import len_browser_open

class TestBrowser(unittest.TestCase):
    @patch('browser.browser_open')
    def test_browser_open(self, mock_browser_open):
        mock_browser_open.return_value = 'one'
        self.assertEqual(len_browser_open)