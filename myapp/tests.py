from django.test import TestCase
from django.urls import reverse

# yet another new comment to create a push on main and test CI/CD pipeline
# a new comment-ilknur
# Create your tests here.
# create some two unit tests for the home and about views in myapp/views.py
class ViewsTestCase(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
