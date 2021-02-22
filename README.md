#AscaBlog
Bonjour, 
Ci-joint le résultat du test.

Concernant les tâches effectués : 
- Initialisation d’un projet sous django 2 ou 3  ( django 2.2 )
- Création des models du blog 
- Post : Article du blog contenant un titre, une image, une description courte, une description longue enrichie, ainsi qu’une date de parution (par défaut à la date du jour) 
- Commentary : Commentaire d’utilisateurs naviguant sur le blog 
- Ajouter le model Post a l’admin de django pour voir en ajouter/modifier 
- Créer une page d’accueil qui présente les derniers articles du blog 
--------- Mon accueil contient tous les posts du plus récent au plus ancien.
- Créer une page d’article présentant un article avec les commentaires de l’article. 
- Ajouter la possibilité d’ajouter un commentaire sur la vue d’un article par n’importe quel utilisateur (pas forcément authentifié) 

Concernant les tâches NON effectués : 
- Créer une page de listing des articles incluant tous les articles du blog 
- Bonus : Créer une api pour récupérer les articles ainsi que le détail d’un article avec DjangoRest 
- Chargement des images.
- Ajout de commentaires depuis l'accueil. ( ps : Il est possible d'ecrire un commentaire depuis le menu de l'article ) 
- Une meilleure interface lorsqu'on rentre en détail dans un post.
- Une meilleure interface lorsqu'on rentre dans la page création d'un post.
- Pagination de l'accueil ( post et commentaire )

En bonus : 
- Page de profil contenant uniquement les articles rédigés par l'utilisateur lui-même.
- Page de modification permettant de modifier/supprimer ces propres posts.

Utilisation de : Bootstrap,SQlite3.
Git a été utilisé uniquement à partir de la moitié du projet. Une partie du backend a été développé sans Git.

Pour une raison inconnue, certains fichiers changent leur droit, je devais donc a chaque fois lancer l'app en sudo, y compris pour les commandes git.

Les Comptes disponibles : Axel,Francois
Mot de passe de tous les comptes du bloc azeazeaze123
Le superuser s'ajoute depuis la console avec la commande : sudo python3 manage.py createsuperuser
Il existe deja un superuser : Pseudo:Sevket mdp:123

Environnement : Windows 10 avec invité de commande linux (Ubuntu), atom, DBBrowser, Google Chrome.
