from django import forms
from django.contrib.auth.forms import UserCreationForm
from courses.models import Teacher


class TeacherCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Teacher
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "bio")

