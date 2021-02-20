
from django.urls import path, include
from .  import views

urlpatterns = [
    path('', views.articles_ind, name='articles_ind'),
    path('<str:name>', include('article.urls'),name="article"),

]
