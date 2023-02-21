import unittest
from unittest.mock import patch
import browser

class TestBrowser(unittest.TestCase):

    @patch('browser.BrowserData.browser_open')
    def test_browser_open(self, mock_browser_open):
        mock_browser_open.return_value = 'one'
        self.assertEqual(browser.BrowserData.len_browser_open, 3)


if __name__ == '__main__':
    unittest.main()