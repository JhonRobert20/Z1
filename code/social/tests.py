from django.test import TestCase

from .models import ExtendUser


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        ExtendUser.objects.create(username='jhon', email='jhonbara51214@gmail.com', password="Jhonhola1")

    def test_email_label(self):
        user = ExtendUser.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_user_name_max_length(self):
        user = ExtendUser.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length, 100)