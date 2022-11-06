from django import forms
from .models import Loft
from django.utils.translation import gettext_lazy as _


class AddLoft(forms.ModelForm):
    """ Add new loft form """
    name = forms.CharField(label=_('Loft name'), widget=forms.TextInput(
        attrs={'placeholder': _("Enter loft name"), 'class': 'form-control'}),
                           help_text=_('You can choose any name you want.'))
    latitude = forms.DecimalField(label=_('Latitude'), widget=forms.NumberInput(
        attrs={'placeholder': _('Enter latitude')}),
                                  help_text=_("Your loft's latitude."))
    longitude = forms.DecimalField(label=_('Longitude'), widget=forms.NumberInput(
        attrs={'placeholder': _('Enter longitude')}),
                                   help_text=_("Your loft's longitude."))

    class Meta:
        model = Loft
        fields = '__all__'
        error_messages = {
            'name': {
                'max_length': _("This loft's name is too long."),
            },
            'latitude': {
                'max_length': _('Ensure that there are no more than 9 digits in total.'),
            },
            'longitude': {
                'max_length': _('Ensure that there are no more than 9 digits in total.'),
            },
        }
        widgets = {
            'address': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'class': 'form-control',
                                             'placeholder': _(' Country \n Region/State \n'
                                                              ' Street \n Number')}),
        }
