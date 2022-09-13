from django.contrib import admin
from .models import Pigeon, PigeonLine, Status, Strain, EyeColor, Color, Loft, ClaimRequest


# Register your models here.


@admin.register(Loft)
class LoftAdmin(admin.ModelAdmin):
    pass


@admin.register(Pigeon)
class PigeonAdmin(admin.ModelAdmin):
    pass


@admin.register(PigeonLine)
class PigeonLineAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Strain)
class StrainAdmin(admin.ModelAdmin):
    pass


@admin.register(EyeColor)
class EyeColourAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColourAdmin(admin.ModelAdmin):
    pass


@admin.register(ClaimRequest)
class ClaimRequestAdmin(admin.ModelAdmin):
    pass
