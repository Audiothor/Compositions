from django.urls import path
from settings.views import settings_import

urlpatterns = [
    path('import.html',settings_import),
    # Ajoutez d'autres URLs si nécessaire
]