# -*- coding:utf-8 -*-
from urllib import urlencode
from urllib2 import urlopen
import json
from contextlib import closing


URL = r'http://api.aoikujira.com/hyakunin/get.php?{query}'


def findpoem(keyword):
    """百人一首APIを問い合わせて結果を辞書のリストで返す。"""
    values = {"fmt": "json",
              "key": keyword.encode("utf-8")
                     if isinstance(keyword, unicode) else keyword}
    url = URL.format(query=urlencode(values))
    with closing(urlopen(url)) as response:
        rows = json.loads(response.read())
    return rows
