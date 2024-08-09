from django import forms
from morceaux.models import Style,Instrument

class EditerInstrument(forms.Form):
    nom = forms.CharField(
        label='Name ',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control-sm','size':'50','autofocus': True}))
    repertoire = forms.CharField(
        label='Directory ',
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control-sm','size':'100'}))

class EditerStyle(forms.Form):
    nom = forms.CharField(
        label='Name ',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control-sm','size':'50','autofocus': True}))
        
class EditerMorceau(forms.Form):
    #renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    nom = forms.CharField(
        label='Name ',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control','size':'150','autofocus': True}))
    
    duree = forms.CharField(
        label='Duration ',
        max_length=8,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control-sm','size':'8'}))
    
    date_debut = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control-sm'}),initial=False,required=False)
    date_fin = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control-sm'}),initial=False,required=False)

    instrument = forms.ModelChoiceField(queryset=Instrument.objects.all(),empty_label="")
    style = forms.ModelChoiceField(queryset=Style.objects.all(),empty_label="")

    locked = forms.BooleanField(initial=False,required=False)
    download = forms.BooleanField(label='Accept Download',initial=False,required=False)
    player = forms.BooleanField(label='Accept Player',initial=False,required=False)

    music_file = forms.FileField(label='Music file',required=False)
    image_file = forms.ImageField(label='Image file',required=False)

    mixed = forms.BooleanField(initial=False,required=False)
    finished = forms.BooleanField(initial=False,required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['music_file'].widget.clear_checkbox_label = 'clear'
        #self.fields['music_file'].widget.initial_text = "Current value"
        #self.fields['music_file'].widget.input_text = "Change"

        #self.fields['image_file'].widget.clear_checkbox_label = 'clear'
        #self.fields['image_file'].widget.initial_text = "Current value"
        #self.fields['image_file'].widget.input_text = "Change"




