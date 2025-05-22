from django.urls import path
from courses.views import (
    index,
    TeacherListView,
    TeacherDetailView,
    TeacherUpdateView,
    TeacherDeleteView,
    CourseDetailView,
    CoursesListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    LessonDetailView,
    TeacherCreateView,
    LessonCreateView,
    LessonUpdateView,
    LessonDeleteView,
)

app_name = "courses"


urlpatterns = [
    path("", index, name="index"),
    path("teachers/", TeacherListView.as_view(), name="teacher-list"),
    path("teachers/<int:pk>/", TeacherDetailView.as_view(), name="teacher-detail"),
    path(
        "teachers/<int:pk>/delete/", TeacherDeleteView.as_view(), name="teacher-delete"
    ),
    path(
        "teachers/<int:pk>/update/", TeacherUpdateView.as_view(), name="teacher-update"
    ),
    path("teachers/create/", TeacherCreateView.as_view(), name="teacher-create"),
    path("courses/", CoursesListView.as_view(), name="course-list"),
    path("courses/<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
    path("courses/create/", CourseCreateView.as_view(), name="course-create"),
    path("courses/<int:pk>/update/", CourseUpdateView.as_view(), name="course-update"),
    path("courses/<int:pk>/delete", CourseDeleteView.as_view(), name="course-delete"),
    path("lessons/<int:pk>/", LessonDetailView.as_view(), name="lesson-detail"),
    path("lessons/create/", LessonCreateView.as_view(), name="lesson-create"),
    path("lessons/<int:pk>/update", LessonUpdateView.as_view(), name="lesson-update"),
    path("lessons/<int:pk>/delete/", LessonDeleteView.as_view(), name="lesson-delete"),
]
