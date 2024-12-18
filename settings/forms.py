from django import forms
from .models import Config

class Config(forms.ModelForm):
    class Meta:
        model = Config
        fields = ['display_website_name','news_print_sorted_creation_date','news_print_creation_date','news_print_news_type','news_print_last_five_music','news_print_news','news_text_input_welcome','news_image_input_welcome','news_print_text_welcome','news_print_image_welcome','news_print_number_musics_page','musics_list_view','musics_print_hits']