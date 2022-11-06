""" Writing tests for app breeder. """

from django.test import TestCase

from .models import Breeder


# Create your tests here.


class BreederModelTest(TestCase):
    """ Testing model functions. """

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.Breeder = Breeder.objects.create(
            email='caplat93@gmail.com',
            password='Porumbel93',
            last_name='Caplat',
            first_name='Ionut')

    def test_last_name_label(self):
        breeder = Breeder.objects.get(id=1)
        field_label = breeder._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_surname_max_length(self):
        breeder = Breeder.objects.get(id=1)
        max_length = breeder._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 75)

    def test_breeder_full_name(self):
        breeder = Breeder.objects.get(id=1)
        expected_breeder_name = f'{breeder.last_name} {breeder.first_name}'
        self.assertEqual(expected_breeder_name, breeder.get_full_name())

    def test_breeder_profile_completion(self):
        breeder = Breeder.objects.get(id=1)
        self.assertEqual(breeder.profile_completion, 40)
