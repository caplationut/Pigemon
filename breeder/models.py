from django.db import models
from .modelmanager import BreederManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Breeder(AbstractBaseUser, PermissionsMixin):
    """ Extend the User model to meet the requirements. """

    LANGUAGE_CHOICES = (
        ('en-us', 'English'),
        ('ro-ro', 'Romana'),
    )
    first_name = models.CharField(max_length=75, null=True, blank=True)
    last_name = models.CharField(max_length=75, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    region_state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    picture = models.URLField(blank=True, null=True)
    language = models.CharField(default='en-us', choices=LANGUAGE_CHOICES, max_length=5)

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
