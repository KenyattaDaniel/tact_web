from django.conf.urls import url, include

from . import views

urlpatterns = [
	#Show homepage
	url(r'^$', views.index, name='index'),
	#Show about page
	url(r'^about/$', views.about, name='about'),
	#Show contact page
	url(r'^contact/$', views.contact, name='contact'),
]