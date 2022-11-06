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
        db_index=True,
        verbose_name=_("breeder")
    )
    name = models.CharField(max_length=100,
                            verbose_name=_("name"))
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        verbose_name=_("latitude")
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        verbose_name=_("longitude")
    )
    address = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name=_("address")
    )

    class Meta:
        verbose_name = _('Loft')
        verbose_name_plural = _('Lofts')

    def __str__(self):
        return self.name
