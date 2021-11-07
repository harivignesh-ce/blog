from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignUpPageTests(TestCase):
    def test_signup_page_status_code(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        username = "newuser"
        email = "newuser@email.com"
        get_user_model().objects.create_user(username=username, email=email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, username)
        self.assertEqual(get_user_model().objects.all()[0].email, email)
