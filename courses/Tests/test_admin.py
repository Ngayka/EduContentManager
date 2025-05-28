from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase

from courses.models import Teacher


User = get_user_model()

class AdminTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(
            username="admin",
            email="admin@admin.com",
            password="admin_password")

        self.teacher = User.objects.create_user(
            username="user",
            email="user@user.com",
            password="user_password"
        )
    def test_admin_can_accessed_admin(self):
        self.client.login(username="admin", password="admin_password")
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 200)

    def test_user_can_not_accessed_admin(self):
        self.client.login(username="user", password="user_password")
        response = self.client.get("/admin/")
        self.assertNotEqual(response.status_code, 200)


