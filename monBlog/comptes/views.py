from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/monActivite/')
    else:
        form = UserCreationForm()
    return render(request,'comptes/inscription.html', {'form':form})


def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/monActivite/')
    else:
        form = AuthenticationForm()
    return render(request,'comptes/connexion.html', {'form':form})

def deconnexion(request):
    logout(request)
    return redirect('/')
