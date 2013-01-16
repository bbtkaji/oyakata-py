# -*- coding:utf-8 -*-
import random

from django.views.generic import View
from django.template.response import TemplateResponse

import app.tanka100.api as tanka_api


HIRAGANA = (u"あいうえお"
            u"かきくけこ"
            u"さしすせそ"
            u"たちつてと"
            u"なにぬねの"
            u"はひふへほ"
            u"まみむめも"
            u"やゆよ"
            u"わをん"
            )


class Index(View):
    http_method_names = ["get"]
    template = "top/index.html"

    def get(self, request, *args, **kwargs):
        """ランダムにひらがな一文字を指定して百人一首を検索する。"""
        keyword = random.choice(HIRAGANA)
        rows = tanka_api.findpoem(keyword)
        context = {"rows": rows, "letter": keyword}
        return TemplateResponse(request, self.template, context)
