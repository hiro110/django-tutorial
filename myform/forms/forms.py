from django.forms import ModelForm
from forms.models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('name', 'address',)