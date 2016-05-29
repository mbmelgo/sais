from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Student

# Create your views here.

#views: index, class search, enrol add, enrol drop, grades,
#personal data summary, schedule, finance_summary

#home-page
def index(request):
	b = Student.objects.all()
	# print(b.get().first_name)
	template = loader.get_template('student/index.html')
	context = {
		'current_user': b.get().first_name,
	}

	return HttpResponse(template.render(context, request))

#under self-service
def class_search(request):
	return HttpResponse("This is the class search page")

#under enrolment
def class_add(request):
	return HttpResponse("This is the class add page")

#under enrolment
def class_drop(request):
	return HttpResponse("This is the class drop page")

#under enrolment
def class_grade(request):
	return HttpResponse("This is the class grade page")

#under campus personal information
def std_summary(request):
	return HttpResponse("This is the student information page")

#student center
def std_sched(request):
	return HttpResponse("This is the student schedule page")

#account inquiry
def finance_summary(request):
	return HttpResponse("This is the finance summary page")
