from django.urls import path
from news import views

urlpatterns = [
    #path('<int:id>', views.detail,name="detail"),
    path('',views.news_list,name="news"),
    path('news/',views.news_list,name="news_list"),
    path('news_add',views.news_add,name="news_add"),
    path('news_edit/<int:id>',views.news_edit,name="news_edit"),
    path('news_delete/<int:id>',views.news_delete,name="news_delete"),
    path('news_publish/<int:id>',views.news_publish,name="news_publish"),
    #path('search/', views.search_news, name='blog-search-post'),
]
