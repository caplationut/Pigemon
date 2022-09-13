""" Writing tests for app breeder. """

from django.test import TestCase
from graphene_django.utils import GraphQLTestCase

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


class TestBreederGraphql(GraphQLTestCase):
    GRAPHQL_URL = "/graphql"

    def test_breeders_query(self):
        """Test GraphQL query for breeders list."""
        resp = self.query(
            '''
            query {
                breeders {
                    firstName,
                    lastName,
                    email
                }
            }
            '''
        )

        self.assertResponseNoErrors(resp)

    def test_breeder_query_by_id(self):
        """Test GraphQL query for breeder by id."""
        Breeder.objects.create_user("test@test.com", 'passw0rd')
        resp = self.query(
            '''
            query {
                breeder(id: 1) {
                    firstName,
                    lastName,
                    email
                }
            }
            '''
        )

        self.assertResponseNoErrors(resp)

    def test_breeder_creation_mutation(self):
        """Test breeder creation mutation."""
        resp = self.query(
            '''
            mutation {
                register(
                        email: "test1@te.com",
                        password1: "pa55w0rd",
                        password2: "pa55w0rd"
                     ) {
                    success,
                    errors
                }
            }
            '''
        )

        self.assertResponseNoErrors(resp)
