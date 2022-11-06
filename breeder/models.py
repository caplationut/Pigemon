from django.db import models
from .modelmanager import BreederManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Breeder(AbstractBaseUser, PermissionsMixin):
    """ Extend the User model to meet the requirements. """

    LANGUAGE_CHOICES = (
        ('en-us', _('English')),
        ('ro', _('Romanian')),
        ('fr', _('French')),
        ('nl', _('Dutch')),
        ('de', _('German')),
        ('it', _('Italian')),
        ('es', _('Spanish')),

    )
    first_name = models.CharField(
        max_length=75,
        null=True,
        blank=True,
        verbose_name=_("first name")
    )
    last_name = models.CharField(
        max_length=75,
        null=True,
        blank=True,
        verbose_name=_("last name")
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name=_("email")
    )
    phone_number = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        verbose_name=_("phone number")
    )
    address = models.CharField(
        max_length=254,
        blank=True,
        null=True,
        verbose_name=_("address")
    )
    region_state = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("region state")
    )
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("country")
    )
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_("date joined"))
    last_login = models.DateTimeField(null=True,blank=True, verbose_name=_("last login"))
    last_updated = models.DateTimeField(auto_now=True, verbose_name=_("last updated"))
    is_staff = models.BooleanField(default=False, verbose_name=_("is staff"))
    is_superuser = models.BooleanField(default=False, verbose_name=_("is superuser"))
    is_active = models.BooleanField(default=True, verbose_name=_("is active"))
    is_verified = models.BooleanField(default=False, verbose_name=_("is verified"))
    picture = models.URLField(blank=True, null=True, verbose_name=_("picture"))
    language = models.CharField(
        default='en-us',
        choices=LANGUAGE_CHOICES,
        max_length=5,
        verbose_name=_("language")
    )

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = BreederManager()

    class Meta:
        verbose_name = _("Breeder")
        verbose_name_plural = _("Breeders")
        ordering = ['-date_joined']

    def get_full_name(self):
        """ Returns the full name of the breeder. """
        return '%s %s' % (self.last_name, self.first_name)

    @property
    def profile_completion(self):
        """ Calculation of the profile completion percentage. """
        percent = {'last_name': 20, 'first_name': 20, 'phone_number': 10,
                   'address': 10, 'region_state': 15, 'country': 10,
                   'picture': 5, 'language': 10,
                   }
        total = 0

        for k, v in percent.items():
            if getattr(self, k):
                total += v
        return total

    def __str__(self):
        return self.email
