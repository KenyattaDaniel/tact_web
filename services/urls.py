from django.conf.urls import url, include

from . import views

urlpatterns = [
	# Show all categories
	url(r'^$', views.categories, name='categories'),
	# Detail page for a category
	url(r'^(?P<category_title_slug>[\w\-]+)/$', views.category, name='category'),
	# Detail page for a single service
	url(r'^(?P<category_title_slug>[\w\-]+)/(?P<service_title_slug>[\w\-]+)/$', views.service, name='service'),
]