from django import forms
from . import models
from django.contrib.auth.models import User

class NewPost(forms.ModelForm):
    class Meta:
        model = models.Ascapost
        fields = ['titre','image','description_courte','description_longue']
        exclude = ['auteur']

    def __init__(self, *args, **kwargs):
        super(NewPost, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class NewCommentaire(forms.ModelForm):
    class Meta:
        model = models.Commentary
        fields = ['commentaire']
        exclude = ['ascanien','article_cible']

    def __init__(self, *args, **kwargs):
        super(NewCommentaire, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
