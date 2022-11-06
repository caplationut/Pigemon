from django import forms
from django.utils.translation import gettext_lazy as _
from .models import *


class AddPigeon(forms.ModelForm):

    sire = forms.ModelChoiceField(queryset=None, empty_label=_("Choose sire"), label=_("Sire"), required=False,
                                  widget=forms.Select(attrs={'type': 'text', 'id': 'select-sire',
                                                             'class': 'form-select'})
                                  )
    dam = forms.ModelChoiceField(queryset=None, empty_label=_("Choose dam"), label=_("Dam"), required=False,
                                 widget=forms.Select(attrs={'type': 'text',
                                                            'class': 'form-select'})
                                 )
    status = forms.ModelChoiceField(queryset=None, empty_label=_("Select status"), label=_("Status"), required=False,
                                    widget=forms.Select(attrs={'type': 'text',
                                                               'class': 'form-select'})
                                    )
    color = forms.ModelChoiceField(queryset=None, required=True, empty_label=_("Select color"), label=_("Color"),
                                   widget=forms.Select(attrs={'type': 'text',
                                                              'class': 'form-select'})
                                   )
    eye_color = forms.ModelChoiceField(queryset=None, required=True, empty_label=_("Select color"),
                                       label=_(" Eye color"),
                                       widget=forms.Select(attrs={'type': 'text',
                                                                  'class': 'form-select'})
                                       )
    strain = forms.ModelChoiceField(queryset=None, required=False, empty_label=_("Select strain"),
                                    widget=forms.Select(attrs={'type': 'text',
                                                               'class': 'form-select'})
                                    )
    line = forms.ModelChoiceField(queryset=None, required=False, empty_label=_("Select line"), label=_("Line"),
                                  widget=forms.Select(attrs={'type': 'text',
                                                             'class': 'form-select'})
                                  )

    def __init__(self, *args, breeder=None, **kwargs):
        super(AddPigeon, self).__init__(*args, **kwargs)
        self.fields['sire'].queryset = Pigeon.objects.filter(loft__breeder=breeder, gender__exact="male")
        self.fields['dam'].queryset = Pigeon.objects.filter(loft__breeder=breeder, gender__exact="female")
        # self.fields['sire'].label_from_instance = lambda obj: "%s" % obj.ring_serial
        # self.fields['dam'].label_from_instance = lambda obj: "%s" % obj.ring_serial
        self.fields['strain'].queryset = Strain.objects.filter(loft__breeder=breeder).prefetch_related('strains')
        self.fields['line'].queryset = PigeonLine.objects.filter(loft__breeder=breeder).prefetch_related('lines')
        self.fields['strain'].label_from_instance = lambda obj: "%s" % obj.name
        self.fields['line'].label_from_instance = lambda obj: "%s" % obj.line_name
        self.fields['status'].queryset = Status.objects.all()
        self.fields['status'].label_from_instance = lambda obj: "%s" % _(obj.status)
        self.fields['color'].queryset = Color.objects.all().prefetch_related('pigeons')
        self.fields['color'].label_from_instance = lambda obj: "%s" % _(obj.color)
        self.fields['eye_color'].queryset = EyeColor.objects.all().prefetch_related('pigeons')
        self.fields['eye_color'].label_from_instance = lambda obj: "%s" % _(obj.eye_color)
        self.fields['loft'].initial = Loft.objects.get(breeder=breeder).id

    class Meta:
        model = Pigeon
        fields = "__all__"
        widgets = {
            'pigeon_country_code': forms.TextInput(attrs={
                'class': 'form-control', 'title': _("Pigeon country code"), 'placeholder': _("Country"),
                'list': 'countryOptions'
            }),
            'pigeon_organisation': forms.TextInput(attrs={
                'class': 'form-control', 'title': _("Pigeon Organisation"), 'placeholder': _("Organisation"),
            }),
            'pigeon_ring_number': forms.NumberInput(attrs={
                'class': 'form-control', 'title': _("The numbers on the pigeon ring"), 'placeholder': _("Digits"),
            }),
            'ring_year': forms.NumberInput(attrs={
                'class': 'form-control', 'title': _("Hatch year"), 'placeholder': _("Year"),
            }),
        }
