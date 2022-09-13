from django.contrib import admin
from .models import Breeder


@admin.register(Breeder)
class BreederAdmin(admin.ModelAdmin):
    """Breeder admin model."""
    readonly_fields = ['password']
