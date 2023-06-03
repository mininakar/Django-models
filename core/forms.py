from django import forms
from core import models

class MedSearch (forms.Form):
    name = forms.CharField (label = 'Поиск по названию препарата', required = False)
    def clean_name (self):
        name = self.cleaned_data['name']
        if '/' in name:
            raise forms.ValidationError('Изыините, имя не должно содержать специальных символов')
        return name


class MedCreate (forms.ModelForm):
    price = forms.FloatField (label="Цена", min_value=0, required=False)
    class Meta:
        model = models.Medicines
        fields = '__all__'

