from django.forms import forms, CharField, ModelForm, URLField

from main.models import DishofMan
from main.widgets import ImageWidget


class HomeSearchForm(forms.Form):
    search_query = CharField(max_length=1000, label='I Want')


class DishofManForm(ModelForm):
    img = URLField(widget=ImageWidget, label='Look')

    class Meta:
        model = DishofMan
        fields = ['img', 'label', 'type', 'price', 'restaurant']

    class Media:
        css = {
            'all': ['css/dishofmanform.css'],
        }
        js = []