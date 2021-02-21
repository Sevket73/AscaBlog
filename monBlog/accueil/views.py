from django.shortcuts import render
from monActivite.models import Ascapost

# Create your views here.
def index(request):
    articles = Ascapost.objects.all().order_by('-id')
    data = {'articles': articles}
    return render(request, 'accueil/index.html',data)
