from django.urls import path
from courses.views import index


app_name = 'courses'
urlpatterns = [
    path('courses/', index, name='index'),
]