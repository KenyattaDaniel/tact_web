from django.conf.urls import url, include

from . import views

urlpatterns = [
	# Show all service categories
	url(r'^$', views.services, name='services'),
	# Detail page for a service category
	url(r'service/(?P<service_id>\d+)/$', views.service, name='service'),
	# Detail page for a single offering
	url(r'offering/(?P<offering_id>\d+)/$', views.offering, name='offering'),
]