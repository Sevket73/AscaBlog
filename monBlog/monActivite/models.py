from django.db import models
from django.contrib.auth.models import User


class Ascapost(models.Model):
    titre = models.TextField(default='AscaTitre', max_length=400)
    image = models.ImageField(upload_to = 'imageBDPost/', default = 'imageBDPost/imagevide.png')
    description_courte = models.TextField(default='AscaDescription_courte', max_length=280 ) #Sera afficher lorsqu'un Ascanien a une vue globale sur tous les articles
    description_longue = models.TextField(default='AscaDescription_longue') #Sera afficher lorsqu'un Ascanien a une vue d'un article en détail
    auteur =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.titre

#ici la liste des commentaires de tous les articles
class Commentary(models.Model):
    ascanien = models.ForeignKey(User, on_delete=models.CASCADE, default='Anonyme')
    commentaire = models.TextField(max_length=280)
    date = models.DateField(auto_now=True)
    article_cible = models.ForeignKey(Ascapost, on_delete=models.CASCADE, default='Ascapost') #cette ligne permet de faire le lien entre le commentaire et l'article concerné

    def __str__(self):
        return self.commentaire
