from django.conf.urls import url
from . import views

urlpatterns = [
    url('inscription/',views.inscription,name="inscription"),
    url('login/',views.connexion,name="connexion"),
    url('deconnexion/',views.deconnexion,name="deconnexion")
]
