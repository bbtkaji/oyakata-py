# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url

import app.top.views as views


urlpatterns = patterns('',
    url(r'$', views.Index.as_view())
)
