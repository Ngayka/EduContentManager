from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Teacher(AbstractUser):
    bio = models.TextField(blank=True)

    def __str__(self):
        return (
            f"{self.username}: "
                f"{self.first_name} "
                f"{self.last_name}. "
                f"{self.bio}"
        )

    def get_absolute_url(self):
        return reverse(
            "courses:teacher-detail", kwargs={"pk": self.pk}
        )


class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    teacher = models.ManyToManyField(Teacher, related_name="courses")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons"
    )
    video_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title}, {self.content}"
