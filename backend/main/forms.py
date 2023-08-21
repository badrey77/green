from django.forms import forms, CharField


class HomeSearchForm(forms.Form):
    search_query = CharField(max_length=1000, label='I Want')