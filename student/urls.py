from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# url(r'/class_search/$', views.class_search, name='search')

	url(r'^classes/class_search/', 'student.views.class_search', name='search'),
    url(r'^classes/class_add/', 'student.views.class_add', name='add'),
    url(r'^classes/class_drop/', 'student.views.class_drop', name='drop'),
    url(r'^classes/grades/', 'student.views.class_grade', name='grade'),
    url(r'^personalinfo/basic/', 'student.views.std_summary', name='summary'),
    url(r'^studentcenter/home/', 'student.views.std_sched', name='schedule'),
    url(r'^finance/home/', 'student.views.finance_summary', name='finance'),
]