from django import forms
from news.models import News
from morceaux.models import Morceau

class EditNews(forms.Form):
    #morceau_all=Morceau.objects.values_list('id',flat=True)
    title = forms.CharField(
        label='Title ',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control-sm','size':'50','autofocus': True}))
    LIST_TYPE = [("",""),("New music","New music"),("Information","Information"),("Concert","Concert")]
    type=forms.ChoiceField(choices=LIST_TYPE)
    morceau=forms.ModelChoiceField(queryset=Morceau.objects.all(),empty_label="",required=False)
    comment=forms.CharField(widget=forms.Textarea,required=False)
    order=forms.IntegerField(initial=1,required=False)
    date_creation=forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control-sm'}),initial=False,required=False)
    start_publication=forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control-sm'}),initial=False,required=False)
    end_publication=forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control-sm'}),initial=False,required=False)
    activated=forms.BooleanField(initial=False,required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)