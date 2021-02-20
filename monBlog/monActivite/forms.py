from django import forms
from . import models

class NewPost(forms.ModelForm):
    class Meta:
        model = models.Ascapost
        fields = ['titre','image','description_courte','description_longue','auteur']

class NewCommentaire(forms.ModelForm):
    class Meta:
        model = models.Commentary
        fields = ['ascanien','commentaire','article_cible']

# edit
# # Creating a form to change an existing article.
# >>> article = Article.objects.get(pk=1)
# >>> form = ArticleForm(instance=article)
