from django import forms
from .models import Config

class Config(forms.ModelForm):
    class Meta:
        model = Config
        fields = ['display_website_name','news_print_sorted_creation_date','news_print_creation_date','news_print_news_type','news_print_last_five_music']