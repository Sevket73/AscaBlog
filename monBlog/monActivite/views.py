from django.shortcuts import render, redirect
from .models import Ascapost, Commentary
from django.contrib.auth.decorators import login_required
from .import forms


@login_required(login_url='/comptes/inscription/')
def monActivite_ind(request):
    articles = Ascapost.objects.all()
    data = {'articles': articles}
    return render(request,'monActivite/monActivite_ind.html', data)

def article_page(request, id):
    try:
        mon_article = Ascapost.objects.get(id=id)
        form = forms.NewCommentaire()
        data = {'form': form, 'article': mon_article}
        if request.method == 'POST':
            form = forms.NewCommentaire(request.POST)
            form.ascanien = request.user
            form.article_cible = mon_article
            if form.is_valid():
                form.save()
                return redirect('/monActivite/')
        else:
            form = forms.NewCommentaire()
            #form = forms.NewCommentaire({'article_cible': mon_article,'ascanien': request.user})
            data = {'form': form, 'article': mon_article}
        return render(request,'monActivite/article_ind.html',data)
    except Exception as e:
        print(e)
        data = {'message': 'l\'article n\'existe pas','form': form, 'article': mon_article}
        return render(request,'monActivite/article_ind.html', data)

@login_required(login_url='/comptes/inscription/')
def newAscapost(request):
    if request.method == 'POST':
        form = forms.NewPost(request.POST)#,request.FILES
        if form.is_valid():
            print(form.errors)
            form.save()
            return redirect('/monActivite/')
    else:
        form = forms.NewPost()
        data = {'form': form}
    return render(request,'monActivite/Nouveau_Ascapost_ind.html',data)

def profilAscanien(request, name):
    articles = Ascapost.objects.filter(auteur=name).values()
    data = {'articles': articles}
    return render(request,'monActivite/monActivite_ind.html', data)
