from django.test import (TestCase)
from django.urls import reverse

from courses.models import Teacher, Course, Lesson


class ModelTest(TestCase):
    def test_teacher_str(self):
        teacher = Teacher.objects.create(
            username="teacher",
            first_name="Test",
            last_name="Test_surname",
            bio="Test bio"
        )
        self.assertEqual(str(teacher),
                         f"{teacher.username}: "
                                f"{teacher.first_name} "
                                f"{teacher.last_name}. "
                                f"{teacher.bio}")
    def test_get_absolute_url(self):
        teacher = Teacher.objects.create(
            username="teacher",
            first_name="Test",
            last_name="Test_surname",
            bio="Test bio"
        )
        expected_url = reverse("courses:teacher-detail", kwargs={'pk': teacher.pk})
        self.assertEqual(teacher.get_absolute_url(), expected_url)


    def test_course_str(self):
        course = Course.objects.create(
            title="Test Course",
            description="Test description",
        )
        teacher = Teacher.objects.create(
            username="teacher",
            first_name="Test",
            last_name="Test_surname",
            bio="Test bio"
        )
        course.teacher.add(teacher)
        course.save()
        self.assertEqual(str(course), course.title)

    def test_lesson_str(self):
        course = Course.objects.create(
            title="Test Course",
            description="Test description",
        )
        lesson = Lesson.objects.create(
            title="Test Lesson",
            content="Test content",
            course=course,
        )

        self.assertEqual(str(lesson), f"{lesson.title}, {lesson.content}")