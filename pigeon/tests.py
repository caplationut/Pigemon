from django.test import TestCase

# Create your tests here.
from django.test import TestCase

from breeder.models import Breeder
from .models import Loft, Color, EyeColor, Status, Pigeon


class PigeonModelTest(TestCase):
    """ Testing pigeon model."""

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        breeder = Breeder.objects.create(
            email='caplat93@gmail.com',
            password='Porumbel93',
            last_name='Caplat',
            first_name='Ionut',
        )
        loft = Loft.objects.create(
            breeder=breeder,
            latitude=46.6365585,
            longitude=27.598969,
        )
        colour = Color.objects.create(
            color='Albastru',
        )
        eye_colour = EyeColor.objects.create(
            eye_color='Galben',
        )
        status = Status.objects.create(
            status='Activ',
            in_loft=True,
        )

        cls.Pigeon = Pigeon.objects.create(
            loft=loft,
            pigeon_country_code='RO',
            pigeon_organisation='FCI',
            pigeon_ring_number='233456',
            ring_year=2019,
            color=colour,
            eye_color=eye_colour,
            gender=1,
            section=2,
            status=status,
        )

    def test_pigeon_ring_format(self):
        pigeon = Pigeon.objects.get(id=1)
        ring_format = pigeon.pigeon_country_code + '-' + \
            pigeon.ring_year + '-' + \
            pigeon.pigeon_organisation + '-' + \
            pigeon.pigeon_ring_number
        self.assertEqual(pigeon.ring_serial(), ring_format)

    def test_field_completion(self):
        """ Field completion percentage test. """
        pigeon = Pigeon.objects.get(id=1)
        self.assertEqual(round(pigeon.field_completion, 2), 47.83)
