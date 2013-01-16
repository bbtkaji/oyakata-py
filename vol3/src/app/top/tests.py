# -*- coding:utf-8 -*-
import unittest

from django.test.client import RequestFactory

import app.top.views as views


class IndexViewTest(unittest.TestCase):
    def _callFUT(self):
        func = views.Index.as_view()
        request = self._makeRequest()
        response = func(request)
        return response

    def _makeRequest(self):
        return RequestFactory().get("/test")

    def test_normal(self):
        """正常系。エラーなく処理が終了すればok"""
        response = self._callFUT()
        self.assertEqual(response.template_name, "top/index.html")
        response.render()
        self.assertNotEqual(response.content, "")
