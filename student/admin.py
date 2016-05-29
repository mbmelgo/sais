from django.contrib import admin

from .models import Student
from .models import Instructor
from .models import Subject
from .models import Detail
from .models import Lab
from .models import Scholarship
from .models import Enrollment
from .models import Grade




# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_field = ['title']
	filter_horizontal = ('Detail_id',)

class LabAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_field = ['title']
	filter_horizontal = ('Detail_id',)

class EnrollmentAdmin(admin.ModelAdmin):
	list_display = ('student_id',)
	search_field = ['student_id']
	filter_horizontal = ('subject_id',)

class GradeAdmin(admin.ModelAdmin):
	list_display = ('grade_id',)
	search_field = ['grade_id']
	filter_horizontal = ('subject_id',)

admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Detail)
admin.site.register(Lab, LabAdmin)
admin.site.register(Scholarship)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Grade, GradeAdmin)
