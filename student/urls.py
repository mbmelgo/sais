from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# url(r'/class_search/$', views.class_search, name='search')

]