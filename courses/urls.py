from django.urls import path
from courses.views import (index,
                           TeacherListView,
                           TeacherDetailView,
                           TeacherUpdateView,
                           TeacherDeleteView,
                           CourseDetailView,
                           CoursesListView,
                           LessonListView,
                           LessonDetailView,)

app_name = 'courses'
urlpatterns = [
    path('', index, name='index'),
    path("teachers/", TeacherListView.as_view(), name='teacher-list'),
    path("teachers/<int:pk>/", TeacherDetailView.as_view(), name='teacher-detail'),
    path("teachers/<int:pk>/delete/", TeacherDeleteView.as_view(), name='teacher-delete'),
    path("teachers/<int:pk>/update/", TeacherUpdateView.as_view(), name='teacher-update'),
    path("courses/", CoursesListView.as_view(), name='course-list'),
    path("courses/<int:pk>/", CourseDetailView.as_view(), name='course-detail'),
    path("courses/<int:pk>/lessons/", LessonListView.as_view(), name='lesson-list'),
    path("lessons/<int:pk>/", LessonDetailView.as_view(), name='lesson-detail'),
]