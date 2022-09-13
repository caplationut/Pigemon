""" Manager implementation for registered users. """

from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class BreederManager(BaseUserManager):
    """ Validate user registration. """

    def _create_user(self, email, password, is_staff,
                     is_superuser, is_verified, **extra_fields):
        if not email:
            raise ValueError(_('Enter an email address!'))
        now = timezone.now()
        email = self.normalize_email(email)
        breeder = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_verified=is_verified,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        breeder.set_password(password)
        breeder.save(using=self._db)
        return breeder

    def create_user(self, email, password, **extra_fields):
        """ User creation. """
        breeder = self._create_user(email,
                                    password,
                                    False,
                                    False,
                                    False,
                                    **extra_fields
                                    )
        return breeder

    def create_superuser(self, email, password, **extra_fields):
        """ Superuser creation. """
        admin = self._create_user(email,
                                  password,
                                  True,
                                  True,
                                  True,
                                  **extra_fields
                                  )
        return admin
