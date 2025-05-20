from django.urls import path
from courses.views import index, TeacherListView, TeacherDetailView

app_name = 'courses'
urlpatterns = [
    path('courses/', index, name='index'),
    path("teachers", TeacherListView.as_view(), name='teacher-list'),
    path("teachers/<int:pk>", TeacherDetailView.as_view(), name='teacher-detail'),
]