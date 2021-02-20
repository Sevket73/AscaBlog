
from django.urls import path
from .  import views

urlpatterns = [
    path('', views.article, name='article/article_ind'),
    #path('article', include('article.urls')),

]
