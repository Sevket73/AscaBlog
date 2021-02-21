from django.shortcuts import render
from monActivite.models import Ascapost, Commentary

# Create your views here.
def index(request):
    articles = Ascapost.objects.all().order_by('-id')
    commentaires = Commentary.objects.all()
    data = {'articles': articles,'commentaires':commentaires}
    return render(request, 'accueil/index.html',data)
