from django.urls import path
from courses.views import index


app_name = 'courses'
urlpatterns = [
    path('', index, name='index'),
]