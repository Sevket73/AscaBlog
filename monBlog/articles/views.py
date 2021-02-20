from django.shortcuts import render

def articles_ind(request):
    return render(request,'articles/articles_ind.html')

#def article(request, name):
#    return render(request, 'monActivite/article.html')
