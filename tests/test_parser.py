import unittest

import url_parser
from url_parser import UrlParser

class TestParserHelpers(unittest.TestCase):
    test_url1 = "https://api.theinfatuation.com/services/v3/lists/F2B1C31F-CE16-491F-A42C-DDE3FC3D0C9B?content=_Td6WFoAAAD_EtlBA8CBAa8BIQEWAAAAZ0em4uAArgB5XQAFCdEHBvX6LgQ59FSvjTK2reW84kMYsVL4QURbD32vhrBongF76J_DKzCViFwDEvaMkCX1ZspopJwiZ4wWN2gHeBNzTP70ncPCHQ71EknmiC_5FDVnceDaBUm6KlbdK2gDHgC5P9vdn_o6el6hq5pYSbiYc8ypxHAAAAAAAAABkQGvAQAA71vFPKgACvwCAAAAAABZWg"
    test_url1_id = "F2B1C31F-CE16-491F-A42C-DDE3FC3D0C9B"

    test_url2 = "https://api.theinfatuation.com/services/v3/lists/8FB28969-3423-43E1-BAD9-29A5E2107142?content=_Td6WFoAAAD_EtlBA8CcAsQCIQEWAAAAitcSteABQwEUXQAFCdLTCmujCzt4qyIxvrk8TzxZg0iBGWMpA7uWK2DiM_QiSbotSXShQjG_t8d-QnzLeiB14i-cs-n4ulRe4gp_pVevDYtbrzgLGs50PuF0SnJMhal11nBKBn4GdELnvRTQC0J-gBk5BtbGUGcNhBFG1GQb0HLTP9YOLQ2csLTWOuL1rnFGzwDewChIwP440iAzki4cjqbihE_2sKRdodbvcXUN77B8PnWRAQOegxG0KXIA363n-gu3raNMmXpv9vsMxgcafX7gphS_eyQCLaueFkqI2r4C-QRCrJx6aNRStnjMg8NyJUYB3N4V9l50BKuSVjVr835OWtc1saHDmdiw0RgARMBSfPO-2dyuIsgbApqU8f8AAAGsAsQCAAAX--AtqAAK_AIAAAAAAFla"

    def test_http_parser(self):
        """ http parser gets content """
        parsed_http = url_parser.http_parse(self.test_url1)
        self.assertEqual(parsed_http["id"], self.test_url1_id)

    def test_http_failure(self):
        """ http throws exception if there isn't content """
        self.assertRaises(ValueError, url_parser.http_parse, "fail url")

    def test_dict_unicode_to_utf8(self):
        """ test the dictionary unicode converter works """
        unicode_dict = {
            "item1": u'value1',
            "list2": [u'ab', u'bb'],
            "dict3": {
                "sub1": u'value2'
            }
        }

        desired_dict = {
            "item1": "value1",
            "list2": ["ab", "bb"],
            "dict3": {
                "sub1": "value2"
            }
        }
        converted_dict = url_parser.dict_unicode_to_utf8(unicode_dict)
        self.assertEqual(converted_dict, desired_dict)

if __name__ == '__main__':
    unittest.main()
