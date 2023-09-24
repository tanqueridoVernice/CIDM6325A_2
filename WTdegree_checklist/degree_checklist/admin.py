from django.contrib import admin

# Register your models here.

from degree_checklist.models import College, Department, Semester, Degree, Course, Coursetype, Degreecheck, Student

admin.site.register(College)
admin.site.register(Department)
admin.site.register(Semester)
admin.site.register(Degree)
admin.site.register(Course)
admin.site.register(Coursetype)
admin.site.register(Degreecheck)
admin.site.register(Student)
