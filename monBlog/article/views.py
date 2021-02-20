from django.shortcuts import render

def article(request, name):
    return render(request,'article/article_ind.html')

#def article(request, name):
#    return render(request, 'monActivite/article.html')
