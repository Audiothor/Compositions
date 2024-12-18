from django.db import models

class Config(models.Model):
    display_website_name = models.CharField(max_length=50)
    news_print_sorted_creation_date = models.BooleanField(default=True)
    news_print_creation_date = models.BooleanField(default=True)
    news_print_news_type = models.BooleanField(default=True)
    news_print_last_five_music = models.BooleanField(default=True)
    news_print_news = models.BooleanField(default=True)
    news_print_image_welcome = models.BooleanField(default=True)
    news_print_text_welcome = models.BooleanField(default=True)
    news_text_input_welcome = models.CharField(max_length=50)
    news_image_input_welcome = models.CharField(max_length=50)
    news_print_number_musics_page = models.IntegerField(default=20)
    musics_list_view = models.BooleanField(default=True)
    musics_print_hits = models.BooleanField(default=True)

    def __str__(self):
        return self.display_website_name