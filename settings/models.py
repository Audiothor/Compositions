from django.db import models

class Config(models.Model):
    display_website_name = models.CharField(max_length=50)
    news_print_sorted_creation_date = models.BooleanField(default=True)
    news_print_creation_date = models.BooleanField(default=True)
    news_print_news_type = models.BooleanField(default=True)
    news_print_last_five_music = models.BooleanField(default=True)

    def __str__(self):
        return self.display_website_name