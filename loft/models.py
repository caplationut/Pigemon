"""Loft related models."""
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Loft(models.Model):
    """Breeder loft location. """

    breeder = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name='lofts',
        null=True,
        blank=True,
        db_index=True
    )
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True
    )
    address = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = _('Loft')
        verbose_name_plural = _('Lofts')

    def __str__(self):
        return self.name
