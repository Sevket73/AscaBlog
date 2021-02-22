#AscaBlog

Sur le principe des skyblog, j’ai créé un blog pour les collaborateurs d’Ascanio leur permettant de partager sur divers projets.

Technologies utilisées: Django 2.2, Bootstrap, SQlite3.
Git a été utilisé uniquement à partir de la moitié du projet. Une partie du backend a été développée sans Git.

Deux comptes sont disponibles : Axel et François. Leur mot de passe est azeazeaze123.
Le superuser s'ajoute depuis la console avec la commande : 
sudo python3 manage.py createsuperuser.
Il existe déjà un superuser : 
Pseudo: Sevket 
mdp: 123

Pour une raison que j’ignore, certains fichiers changent leur droit (settings.py), je devais donc à chaque fois lancer l'app en sudo, y compris pour les commandes git.

Tâches réalisées : 
- Initialisation d’un projet sous django 2.2
- Création des models du blog 
- Post : Article du blog contenant un titre, une image, une description courte, une description longue enrichie, ainsi qu’une date de parution (par défaut à la date du jour) 
- Commentary : Commentaire d’utilisateurs naviguant sur le blog 
- Ajout du model Post a l’admin de django pour voir en ajouter/modifier 
- Création d’une page d’accueil qui présente les derniers articles du blog 
-- Mon Accueil contient tous les posts du plus récent au plus ancien.
- Création d’une page d’article présentant un article avec les commentaires de l’article. 
- Possibilité d’ajouter un commentaire sur la vue d’un article par n’importe quel utilisateur (même sans authentification)

En bonus : 
- Page de profil d’un utilisateur contenant uniquement les articles rédigés par l'utilisateur lui-même
- Page de modification pour l’utilisateur lui permettant de modifier/supprimer ses posts 

Tâches non-réalisées : 
- Créer une page de listing des articles incluant tous les articles du blog 
- Création d’une api pour récupérer les articles ainsi que le détail d’un article avec DjangoRest 
- Chargement des images : le chemin des images n’était pas reconnu par le programme.
- Ajout de commentaires depuis l'accueil (Il est possible d'écrire un commentaire depuis le menu de l'article) : je n’ai pas trouvé de solution pour lier les données d’un article à un commentaire dans le template.
- Pagination de l'accueil (post et commentaire)
