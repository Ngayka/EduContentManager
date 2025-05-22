from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, DeleteView, CreateView

from courses.forms import (
    TeacherCreationForm,
    CourseForm,
    TeacherForm,
    LessonForm,
    LessonSearchForm,
    CourseSearchForm,
)
from courses.models import Teacher, Course, Lesson


@login_required(login_url="login")
def index(request):
    num_teachers = Teacher.objects.all().count()
    num_courses = Course.objects.all().count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_teachers": num_teachers,
        "num_courses": num_courses,
        "num_visits": num_visits + 1,
    }

    return render(request, "courses/index.html", context=context)


class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    context_object_name = "teachers"
    paginate_by = 6


class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = Teacher


class TeacherUpdateView(generic.UpdateView):
    form_class = TeacherForm
    model = Teacher
    template_name = "courses/teacher_form.html"

    def get_success_url(self):
        return reverse_lazy("courses:course-detail", kwargs={"pk": self.object.pk})


class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy("courses:teacher-list")


class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherCreationForm
    template_name = "courses/teacher_form.html"
    success_url = reverse_lazy("courses:teacher-list")


class CoursesListView(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = "courses"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title")
        context["search_form"] = CourseSearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        form = CourseSearchForm(self.request.GET)
        if form.is_valid():
            title = form.cleaned_data["title"]
            return Course.objects.filter(title__icontains=title)
        else:
            return Course.objects.all()


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    context_object_name = "course"
    template_name = "courses/course_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        form = LessonSearchForm(self.request.GET)

        if form.is_valid():
            content = form.cleaned_data.get("content")
            lessons = Lesson.objects.filter(content__icontains=content)
        else:
            lessons = Lesson.objects.all()

        context["course"] = course
        context["lessons"] = lessons
        context["search_form"] = form
        return context


class CourseCreateView(CreateView):
    form_class = CourseForm
    template_name = "courses/course_create.html"
    success_url = reverse_lazy("courses:course-list")


class CourseUpdateView(generic.UpdateView):
    form_class = CourseForm
    model = Course
    template_name = "courses/course_form.html"

    def get_success_url(self):
        return reverse_lazy("courses:course-detail", kwargs={"pk": self.object.pk})


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy("courses:course-list")


class LessonListView(LoginRequiredMixin, ListView):
    model = Lesson
    context_object_name = "lessons"
    queryset = Lesson.objects.select_related("course")


class LessonDetailView(LoginRequiredMixin, DetailView):
    model = Lesson


class LessonCreateView(CreateView):
    model = Lesson
    fields = "__all__"
    template_name = "courses/lesson_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "courses:course-detail", kwargs={"pk": self.object.course.pk}
        )


class LessonUpdateView(generic.UpdateView):
    form_class = LessonForm
    model = Lesson
    template_name = "courses/lesson_form.html"

    def get_success_url(self):
        return reverse_lazy("courses:lesson-detail", kwargs={"pk": self.object.pk})


class LessonDeleteView(DeleteView):
    model = Lesson

    def get_success_url(self):
        return reverse_lazy(
            "courses:course-detail", kwargs={"pk": self.object.course.pk}
        )
