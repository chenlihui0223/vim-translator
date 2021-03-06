# -*- coding: utf-8 -*-
import sys
import copy
import os
import unittest

curr_filename = os.path.abspath(__file__)
curr_dir = os.path.dirname(curr_filename)
script_path = os.path.join(curr_dir, "../script")
sys.path.append(script_path)

from translator import BaicizhanTranslator
from translator import BingTranslator
from translator import GoogleTranslator
from translator import HaiciTranslator
from translator import ICibaTranslator
from translator import YoudaoTranslator
from translator import TranslateShell


class TestTranslator(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestTranslator, self).__init__(*args, **kwargs)

    @unittest.skip("Expired")
    def test_baicizhan(self):
        t = BaicizhanTranslator()
        r = t.translate("", "", "naive")
        self.assertTrue(len(r['paraphrase']) != 0 or len(r['explain']))

    @unittest.skip("Skip for GitHub Action")
    def test_bing(self):
        t = BingTranslator()
        r = t.translate("", "", "naive")
        self.assertTrue(len(r['paraphrase']) != 0 or len(r['explain']))

    def test_google(self):
        t = GoogleTranslator()
        r = t.translate("auto", "zh", "naive")
        self.assertTrue(len(r['paraphrase']) != 0 or len(r['explain']))

    def test_haici(self):
        t = HaiciTranslator()
        r = t.translate("", "zh", "naive")
        self.assertTrue(len(r['paraphrase']) != 0 or len(r['explain']))

    @unittest.skip("ciba api was deprecated")
    def test_iciba(self):
        t = ICibaTranslator()
        r = t.translate("", "", "naive")
        self.assertTrue(len(r['paraphrase']) != 0 or len(r['explain']))

    def test_translate_shell(self):
        t = TranslateShell()
        r = t.translate("auto", "zh", "naive")
        self.maxDiff = None
        self.assertTrue(len(r['paraphrase']) != 0 or len(r['explain']))

    def test_youdao(self):
        t = YoudaoTranslator()
        r = t.translate("auto", "zh", "naive")
        self.assertTrue(len(r['paraphrase']) != 0 or len(r['explain']))


if __name__ == "__main__":
    unittest.main()
