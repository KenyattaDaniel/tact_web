from django.conf.urls import url, include
from django.contrib.staticfiles.urls import static

from . import views, settings


urlpatterns = [
    url(r'^$', views.tactics, name='tactics'),
    url(r'tactic/(?P<tactic_id>\d+)/$', views.tactic, name='tactic'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)