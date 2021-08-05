import unittest
import os
import convertor

from pathlib import Path
from convertor.convertors import Encoder

KEY_FILE = Path(os.path.dirname(convertor.__file__)) / 'key'


class TestEncoder(unittest.TestCase):
    def setUp(self):
        self.obj = Encoder(KEY_FILE)

    def test_convert_text1(self):
        self.assertEqual(self.obj.convert_text('a second key word is "commits checked"'),
                         '4 53<0|\||) |<3¥ \^/0|2|) !5 "<0|\/||\/|!75 <#3<|<3|)"')

    def test_convert_text2(self):
        self.assertEqual(self.obj.convert_text('plz write the key words in the email answer "hello, hexteam"'),
                         '|O12 \^/|2!73 7#3 |<3¥ \^/0|2|)5 !|\| 7#3 3|\/|4!1 4|\|5\^/3|2 "#3110, #3><734|\/|"')

    def test_convert_text3(self):
        self.assertEqual(self.obj.convert_text('now is better than never'),
                         '|\|0\^/ !5 83773|2 7#4|\| |\|3\/3|2')


if __name__ == '__main__':
    unittest.main()
