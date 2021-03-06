from __future__ import absolute_import
from django.conf.urls import url
import django.views.i18n
from locking import views

urlpatterns = [
    # verwijst naar een ajax-view voor het lockingmechanisme
    url(r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/lock/$', views.lock),
    url(r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/unlock/$', views.unlock),
    url(r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/is_locked/$', views.is_locked),
    url(r'variables\.js$', views.js_variables, {}, 'locking_variables'),
    url(r'jsi18n/$', django.views.i18n.JavaScriptCatalog.as_view(), {'packages': 'locking'}),
]
