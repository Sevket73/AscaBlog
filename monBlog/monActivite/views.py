from django.shortcuts import render, redirect
from .models import Ascapost, Commentary
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .import forms

# Page "mon profil"
# L'ascanien doit être connecté
@login_required(login_url='/comptes/inscription/')
def monActivite_ind(request):
    articles = Ascapost.objects.filter(auteur_id=request.user.id).order_by('-id').values #Liste de tous les articles de l'ascanien
    commentaires = Commentary.objects.all() #Liste de tous les commentaires (Possibilité de récuperer uniquement ceux des articles d'au dessus)
    data = {'articles': articles,'commentaires':commentaires}
    return render(request,'monActivite/monActivite_ind.html', data)

def article_page(request, id):
    try:
        form = forms.NewCommentaire() # Formulaire vide d'un commentaire
        mon_article = Ascapost.objects.get(id=id) # Article cible
        if request.method == 'POST':
            form = forms.NewCommentaire(request.POST) # Formulaire rempli par l'ascanien
            if form.is_valid():
                form = form.save(commit=False) # On commit sans envoyé dans la BD
                if request.user.is_authenticated: # Si connecté
                    form.ascanien = request.user # Remplissage des cases manquantes
                else:
                    try: # Tentative de récuperation d'un compte anonyme
                        user = User.objects.get(username='Ascanien Anonyme')
                        form.ascanien = user
                    except Exception as e: # Si il n'y a pas de compte anonyme alors on le crée
                        user = User.objects.create_user(username='Ascanien Anonyme',
                                     email='aaa@aaa.com',
                                     password='')
                        form.ascanien = user
                form.article_cible = mon_article
                form.save() # Ajout dans la BD
                return redirect('/')
        else:
            commentaires = Commentary.objects.filter(article_cible=mon_article.id).values() # On recupere les commentaires du post cible
            data = {'form': form, 'article': mon_article,'commentaires':commentaires}
        return render(request,'monActivite/article_ind.html',data)
    except Exception as e:
        print(e)
        data = {'message': 'l\'article n\'existe pas','form': form, 'article': mon_article}
        return render(request,'monActivite/article_ind.html', data)

@login_required(login_url='/comptes/inscription/')
def newAscapost(request): #Création d'un AscaPost
    form = forms.NewPost() #Création d'un formulaire de post vide
    data = {'form': form}
    if request.method == 'POST': # Formulaire rempli par l'ascanien en POST
        form = forms.NewPost(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.auteur = request.user
            form.save()
            return redirect('/monActivite/')
    else:
        form = forms.NewPost()
        data = {'form': form}
    return render(request,'monActivite/nouveau_Ascapost_ind.html',data)

# Si une personne veut voir le profil de qq'un d'autres c'est cette fonction qui se lance
def profilAscanien(request, name):
    mon_article = Ascapost.objects.filter(auteur_id=name).values()
    name = User.objects.get(id=name)
    data = {'articles': mon_article,'auteur':name.username}
    return render(request,'monActivite/profilAscanien_ind.html', data)


@login_required(login_url='/comptes/inscription/')
def editPost(request, id):
    post = Ascapost.objects.get( id=id)
    form = forms.NewPost(instance = post)

    if request.method == 'POST':
        form = forms.NewPost(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('/monActivite/')
    data = {'form' :form}
    return render(request,'monActivite/editPost_ind.html',data)

def deletePost(request, id):
    post = Ascapost.objects.get( id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('/monActivite/')
    data = {'post' :post}
    return render(request,'monActivite/deletePost_ind.html',data)

@login_required(login_url='/comptes/inscription/')
def editComm(request, id):
    post = Commentary.objects.get( id=id)
    form = forms.NewPost(instance = post)

    if request.method == 'POST':
        form = forms.NewPost(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('/monActivite/')
    data = {'form' :form}
    return render(request,'monActivite/editComm_ind.html',data)

def deleteComm(request, id):
    post = Commentary.objects.get( id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('/monActivite/')
    data = {'post' :post}
    return render(request,'monActivite/deleteComm_ind.html',data)
