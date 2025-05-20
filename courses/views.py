from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from courses.models import Teacher, Course


def index(request):
    num_teachers = Teacher.objects.all().count()
    num_courses = Course.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {"num_teachers": num_teachers,
               "num_courses": num_courses,
               "num_visits": num_visits + 1,}

    return render(request, "courses/index.html", context=context)

class TeacherListView(ListView):
    model = Teacher
    context_object_name = "teachers"
    paginate_by = 5

class TeacherDetailView(DetailView):
    model = Teacher

class CoursesListView(ListView):
    model = Course
    context_object_name = "courses"


