from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from courses.models import Course, Teacher, Lesson

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Lesson)
