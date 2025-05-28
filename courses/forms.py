from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from courses.models import Teacher, Lesson, Course


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "email", "bio"]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4, "cols": 40}),
        }


class TeacherCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Teacher
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "bio")


class CourseForm(forms.ModelForm):
    teacher = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta(forms.ModelForm):
        model = Course
        fields = "__all__"


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = "__all__"
        widgets = {
            "content": forms.Textarea(attrs={"rows": 4, "cols": 10}),
        }


class LessonSearchForm(forms.Form):
    content = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Search in lessons",
                "autocomplete": "off",
            }
        ),
    )


class CourseSearchForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Search by course name",
                "autocomplete": "off",
            }
        ),
    )
