from django.shortcuts import render
from monActivite.models import Ascapost, Commentary
from monActivite import forms
from django.contrib.auth.models import User
#from .import forms

# Create your views here.
def index(request):
    try:
        articles = Ascapost.objects.all().order_by('-id')
        commentaires = Commentary.objects.all()
        form = forms.NewCommentaire()
        data = {'articles': articles,'commentaires':commentaires}
        if request.method == 'POST':
            form = forms.NewCommentaire(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                if request.user.is_authenticated:
                    form.ascanien = request.user
                else:
                    try:
                        user = User.objects.get(username='Ascanien Anonyme')
                        form.ascanien = user
                    except Exception as e:
                        user = User.objects.create_user(username='Ascanien Anonyme',
                                     email='aaa@aaa.com',
                                     password='')
                        form.ascanien = user
                form.article_cible = mon_article
                form.save()
                return redirect('/')
        else:
            articles = Ascapost.objects.all().order_by('-id')
            commentaires = Commentary.objects.all()
            form = forms.NewCommentaire()
            data = {'articles': articles,'commentaires':commentaires, 'form':form}
        return render(request, 'accueil/index.html',data)
    except Exception as e:
        print(e)
        form = forms.NewCommentaire()
        data = {'message': e,'form': form, 'article': articles}
        return render(request,'accueil/index.html', data)


    if request.method == 'POST':
        form = forms.NewCommentaire(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.user.is_authenticated:
                form.ascanien = request.user
            else:
                try:
                    user = User.objects.get(username='Ascanien Anonyme')
                    form.ascanien = user
                except Exception as e:
                    user = User.objects.create_user(username='Ascanien Anonyme',
                                 email='aaa@aaa.com',
                                 password='')
                    form.ascanien = user
            form.article_cible = mon_article
            form.save()
            return redirect('/')
    else:
        commentaires = Commentary.objects.filter(article_cible=mon_article.id).values()
        data = {'form': form, 'article': mon_article,'commentaires':commentaires}
    return render(request,'monActivite/article_ind.html',data)
