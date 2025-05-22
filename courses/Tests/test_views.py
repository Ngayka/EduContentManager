from datetime import datetime, timezone

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from courses.models import Course, Teacher

COURSE_LIST_URL = reverse("courses:course-list")

class CourseSearchName(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password"
        )
        self.client.force_login(self.user)
        self.teacher = Teacher.objects.create(
            username="test",
            first_name="test",
            last_name="test",
            email="example@test.com",
            password="test_1234"
        )
        self.course_1 = Course.objects.create(
            title="Test Course",
            description="Test Course Description",
        )
        self.course_1.teacher.add(self.teacher)
        self.course_1.save()

        self.course_2 = Course.objects.create(
            title="New-test Course",
            description="new-test Course Description",
        )
        self.course_2.teacher.add(self.teacher)
        self.course_2.save()

    def test_course_search_name(self):
        response = self.client.get(COURSE_LIST_URL)
        self.assertEqual(response.status_code, 200)

        courses = response.context["courses"]

        self.assertEqual(len(courses), 2)
        self.assertEqual(courses[0].title, "Test Course")

    def test_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse("courses:course-list"))
        expected_url = reverse("login") + "?next=" + reverse("courses:course-list")
        self.assertRedirects(response, expected_url)

    def test_create_course(self):
        url = reverse("courses:course-create")
        response = self.client.post(url, data={
            "title": "Test Course",
            "description": "Test Course Description",
        })
        self.assertEqual(Course.objects.count(), 3)