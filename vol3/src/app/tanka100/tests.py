# -*- coding:utf-8 -*-
import unittest

import app.tanka100.api as api


class FindPoemTest(unittest.TestCase):
    def _callFUT(self, keyword):
        return api.findpoem(keyword)

    def test_with_full_name(self):
        """フルネームで絞り込むと1件取得できること。"""
        result = self._callFUT(u"柿本人麻呂")

        self.assertEqual(len(result), 1)

    def test_with_partial_name(self):
        """部分一致で絞り込むと複数件取得できること。"""
        result = self._callFUT(u"麻呂")

        self.assertEqual(len(result), 2)
        authors = [x["sakusya"] for x in result]
        self.assertIn(u"柿本人麻呂", authors)
        self.assertIn(u"阿倍仲麻呂", authors)

    def test_with_strunicode(self):
        """str, unicode型のどちらを引数に渡してもエラーにならないこと。"""
        for x in ("柿本人麻呂", u"柿本人麻呂"):
            result = self._callFUT(x)
            self.assertEqual(len(result), 1)
