from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^$', views.tactics, name='tactics'),
    url(r'tactic/(?P<tactic_id>\d+)/$', views.tactic, name='tactic'),
]

