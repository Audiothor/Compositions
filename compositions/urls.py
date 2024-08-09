"""
URL configuration for compositions project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from website.views import index,welcome,about,biography
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome.html',welcome,name="welcome"),
    path('about.html',about),
    # URLS de l'index
    path('',index,name="index"),
    # URLS de la biographie
    path('biography',biography,name="biography"),
    # URLS de morceaux
    path('morceaux/',include('morceaux.urls')),
    # URL de login
    path('auth/',include('django.contrib.auth.urls')),
    # URL de settings
    path('settings/',include('settings.urls')),
    # URL de news
    path('news/',include('news.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
