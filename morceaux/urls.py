from django.urls import path
from morceaux import views

urlpatterns = [
    path('<int:id>', views.detail,name="detail"),
    path('',views.morceaux_list,name="morceaux"),
    path('styles',views.styles_list,name="styles"),
    path('morceau_nouveau',views.morceau_nouveau,name="morceau_nouveau"),
    path('morceau_editer/<int:id>',views.morceau_editer,name="morceau_editer"),
    path('morceau_supprimer/<int:id>',views.morceau_supprimer,name="morceau_supprimer"),
    path('search/', views.search_morceau, name='blog-search-post'),
    path('instruments/',views.instruments_list,name="instruments_list"),
    path('instrument_editer/<int:id>',views.instrument_editer,name="instrument_editer"),
    path('instrument_supprimer/<int:id>',views.instrument_supprimer,name="instrument_supprimer"),
]
