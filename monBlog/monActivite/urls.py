
from django.urls import path, include
from .  import views

urlpatterns = [
    path('', views.monActivite_ind, name='monActivite_ind'),
    path('article/<str:name>/', views.article_page, name='article_ind'),
    path('Nouveau_Ascapost/', views.newAscapost, name='Nouveau_Ascapost_ind'),
]
