from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from courses.forms import TeacherCreationForm
from courses.models import Teacher, Course, Lesson


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
    paginate_by = 6

class TeacherDetailView(DetailView):
    model = Teacher

class TeacherUpdateView(UpdateView):
    model = Teacher
    success_url = reverse_lazy("courses:teacher-detail")

class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy("courses:teacher-list")

class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherCreationForm
    template_name = "courses/teacher_create.html"
    success_url = reverse_lazy("courses:teacher-list")


class CoursesListView(ListView):
    model = Course
    context_object_name = "courses"

class CourseDetailView(DetailView):
    model = Course
    context_object_name = "course"
    template_name = 'courses/course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lessons"] = self.get_object().lessons.all()
        return context

class LessonListView(ListView):
    model = Lesson
    context_object_name = "lessons"
    queryset = Lesson.objects.select_related("course")

class LessonDetailView(DetailView):
    model = Lesson


