from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^$', views.tactics, name='tactics'),
    url(r'^page/(?P<page>\d+)$', views.tactics, name='archive'),
    url(r'^(?P<slug>.*)$', views.tactic, name='tactic'),
]

