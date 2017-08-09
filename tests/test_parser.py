import unittest

import url_parser
from url_parser import UrlParser

class TestParserHelpers(unittest.TestCase):

    def test_upper(self):
        parsed_http = url_parser.http_parse("https://docs.python.org/hello")
        self.assertEqual(parsed_http, 'FOO')

if __name__ == '__main__':
    unittest.main()