from django.db import models

# Create your models here.
from loft.models import Loft
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


# TODO: refactor pigeon filed names

class PigeonLine(models.Model):
    """ Pigeon line model defining.

        A line of pigeons is made up of a number n
        of pigeons that are related to each other.
        This means that they have the same ancestors.
        It is founded by two pigeons (male, female)
        and the matings are made using the offspring
        of this pair.
    """

    loft = models.ManyToManyField(
        Loft,
        related_name='lines',
        db_index=True
    )
    line_name = models.CharField(max_length=30)
    founder_pigeon = models.CharField(max_length=25)
    notes = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = _("Pigeon line")
        verbose_name_plural = _("Pigeon lines")
        ordering = ['line_name']

    def __str__(self):
        return self.line_name


class Strain(models.Model):
    """ Pigeon strain model defining.

        A strain of pigeon is formed by crossing
        two or more pigeons from different breeders.
        They unite and homogenize over time and after a
        while we will notice that they have the same
        phenotypic features. It can be associated with
        a family whose children resemble their parents.
    """

    SHORT_DISTANCE = 1
    MIDDLE_DISTANCE = 2
    LONG_DISTANCE = 3
    MARATHON = 4

    CATEGORIES = [
        (SHORT_DISTANCE, _('Short distance')),
        (MIDDLE_DISTANCE, _('Middle distance')),
        (LONG_DISTANCE, _('Long distance')),
        (MARATHON, _('Marathon')),
    ]

    loft = models.ManyToManyField(
        Loft,
        related_name='strains',
        db_index=True
    )
    name = models.CharField(max_length=50)
    creator_full_name = models.CharField(max_length=60)
    country = models.CharField(max_length=30, null=True, blank=True)
    category = models.IntegerField(choices=CATEGORIES)
    notes = models.TextField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = _('Strain')
        verbose_name_plural = _('Strains')
        ordering = ['name']

    def __str__(self):
        return self.name


class Color(models.Model):
    """Pigeon color values."""

    color = models.CharField(max_length=30, unique=True, db_index=True)

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')
        ordering = ['color']

    def __str__(self):
        return self.color


class EyeColor(models.Model):
    """Pigeon eye color values."""

    eye_color = models.CharField(max_length=20, unique=True, db_index=True)

    class Meta:
        verbose_name = _('Eye color')
        verbose_name_plural = _('Eye colors')
        ordering = ['eye_color']

    def __str__(self):
        return self.eye_color


class Status(models.Model):
    """Pigeon status choices."""

    status = models.CharField(max_length=15, unique=True, db_index=True)
    in_loft = models.BooleanField()
    color = models.CharField(max_length=7)

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')
        ordering = ['status']

    def __str__(self):
        return self.status


class Pigeon(models.Model):
    """Defining pigeon model.
    ATTENTION: WHEN ADDING A NEW FIELD MAKE SURE YOU ADD IT TO field_completion
    IF IT COUNTS.
    """

    class Gender(models.TextChoices):
        MALE = _('male')
        FEMALE = _('female')
        UNKNOWN = _('unknown')

    class Section(models.TextChoices):
        NEW_ENTRY = _('new_entry')
        YOUNG_BIRD = _('young_bird')
        OLD_BIRD = _('old_bird')
        BREEDING = _('breeding')
        WIDOW_HEN = _('widow_hen')
        WIDOW_COCK = _('widow_cock')
        QUARANTINE = _('quarantine')

    loft = models.ForeignKey(
        Loft,
        on_delete=models.SET_NULL,
        related_name='pigeons',
        null=True,
        db_index=True
    )
    pigeon_organisation = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.PROTECT,
        related_name='pigeons',
        db_index=True
    )
    eye_color = models.ForeignKey(
        EyeColor,
        on_delete=models.PROTECT,
        related_name='pigeons',
        db_index=True
    )
    strain = models.ForeignKey(
        Strain,
        on_delete=models.SET_NULL,
        related_name='pigeons',
        null=True,
        blank=True,
        db_index=True
    )
    line = models.ForeignKey(
        PigeonLine,
        on_delete=models.SET_NULL,
        related_name='pigeons',
        null=True,
        blank=True,
        db_index=True
    )
    sire = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='sire_childs',
        null=True,
        blank=True,
        db_index=True
    )
    dam = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='dam_childs',
        null=True,
        blank=True,
        db_index=True
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='pigeons',
        db_index=True
    )
    date_added = models.DateField(auto_now_add=True)
    pigeon_country_code = models.CharField(max_length=10)
    pigeon_ring_number = models.CharField(max_length=10)
    ring_year = models.CharField(max_length=4)
    gender = models.CharField(choices=Gender.choices, max_length=32)
    hatch_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    section = models.CharField(choices=Section.choices, max_length=32)
    # To avoid a pigeon being deleted from the database and not
    # appearing in the pedigree, when deleting it or the breeder,
    # we will set is_hidden = True
    is_hidden = models.BooleanField(default=False)
    # Is used to highlight the pigeon in the pedigree
    is_best = models.BooleanField(default=False)

    # On each status changes, 'event_date' must be updated
    # with the current date.
    event_date = models.DateField(null=True, blank=True)
    vaccine_date = models.DateField(null=True, blank=True)

    # All info about pigeon
    info = models.TextField(null=True, blank=True)

    # Just few notable info that appear on pedigree
    other_info = models.TextField(max_length=350, null=True, blank=True)

    picture = models.URLField(null=True, blank=True)
    eye_picture = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = _('Pigeon')
        verbose_name_plural = _('Pigeons')
        ordering = ['loft', 'pigeon_country_code']
        unique_together = [
            'pigeon_country_code',
            'pigeon_ring_number',
            'pigeon_organisation',
            'ring_year'
        ]

    @property
    def children(self):
        if self.gender == 1:
            return self.sire_childs.all()
        return self.dam_childs.all()

    def field_completion(self):
        """ Calculation of the pigeon field completion percentage. """
        filled_fields_count = 0
        watched_fields = [
            'loft',
            'pigeon_organisation',
            'color',
            'eye_color',
            'strain',
            'line',
            'sire',
            'dam',
            'status',
            'date_added',
            'pigeon_country_code',
            'pigeon_ring_number',
            'ring_year',
            'gender',
            'hatch_date',
            'name',
            'section',
            'vaccine_date',
            'info',
            'other_info',
            'picture',
            'eye_picture'
        ]

        for field in watched_fields:
            if getattr(self, field):
                filled_fields_count += 1

        if filled_fields_count == 0:
            return 0

        return 100 / (len(watched_fields) / filled_fields_count)

    def ring_serial(self):
        return (f'{self.pigeon_country_code}-{self.ring_year}-'
                f'{self.pigeon_organisation}-{self.pigeon_ring_number}')

    def __str__(self):
        return f'{self.pigeon_country_code} {self.pigeon_ring_number}'


class ClaimRequest(models.Model):
    """Claim request model used by breeders to claim that a pigeon is registered
     illegally in platform by other breeder."""

    class Status(models.IntegerChoices):
        OPEN = 0
        ACCEPTED = 1
        DENIED = 2

    pigeon = models.ForeignKey(
        Pigeon,
        on_delete=models.CASCADE,
        related_name='claim_requests'
    )

    initiator = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='claim_requests'
    )

    proof_picture = models.URLField()
    comments = models.TextField(max_length=300, blank=True, null=True)

    status = models.IntegerField(choices=Status.choices, default=Status.OPEN)
    admin_resolution = models.CharField(max_length=500, blank=True, null=True)
