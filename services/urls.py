from django.conf.urls import url, include

from . import views

urlpatterns = [
	# Show all categories
	url(r'^$', views.categories, name='categories'),
	# Detail page for a category
	url(r'category/(?P<category_id>\d+)/$', views.category, name='category'),
	# Detail page for a single service
	url(r'(?P<service_id>\d+)/$', views.service, name='service'),
]