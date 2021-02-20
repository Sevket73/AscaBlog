
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .  import views

urlpatterns = [
    path('', views.monActivite_ind, name='monActivite_ind'),
    path('article/<int:id>/', views.article_page, name='article_ind'),
    path('Nouveau_Ascapost/', views.newAscapost, name='Nouveau_Ascapost_ind'),
    path('Ascanien/<str:name>/', views.profilAscanien, name='profilAscanien_ind'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
