=============================================
Technologies et les langages de programmation
=============================================

.

.. _Python: https://www.python.org/

.. _Django: https://www.djangoproject.com/

.. _Docker: https://www.docker.com/

.. _Sentry: https://sentry.io/welcome/

.. _GitHub: https://github.com/

.. _AWS EC2: https://docs.aws.amazon.com/fr_fr/AWSEC2/latest/UserGuide/concepts.html

.. _Dockerfile: procedures-de-deploiement-et-de-gestion.html

.. _.env: guide-de-demarrage-rapide.html

.. _installation: installation.html

.. _here: procedures-de-deploiement-et-de-gestion.html

Plusieurs technologies et langages sont utilisés pour ce projet. 
Assurez-vous de comprendre et de les installer correctement pour une expérience de développement sans heurts.

Python_
^^^^^^^^

C'est le langage de programmation utilisé dans ce projet suite à son polyvalent et puissant. 
Il ets donc necessaire d'installer cette langage dans votre ordinateur pour l'utilisation.

Django_
^^^^^^^^

C'est un fraimework web utilisé dans ce projet. 
Il est noté dans le fichier requirements.txt du projet et à installer dans l'environnement virtuel.

Django SECRET_KEY pour ce projet est configuré default quand besoin, 
vous pouvez ajouter votre Django Secret_key dans fichier `.env`_

Docker_
^^^^^^^^

C'est une plateforme permettant de lancer ce projet dans un conteneur isolé, qui pourra être ecécute sur n'importe quel serveur.
Dans ce projet, les commandes sont faites dans fichiers Dockerfile_ et docker-compose.yml

Sentry_
^^^^^^^

C'est une plateforme de surveillance des eurreurs et performance.

Le DSN de ce projet doivent être ajouter dans le fichier `.env``

GitHub_
^^^^^^^^

C'est une platforme pour stocker et manager votre code. 
Il est utilisé pour la control version et collaboration.

Nous utilisant trunk base management pour une bon structure d'organation des control version.

Les demarche du git pour ce projet se trouver dans installation_

`AWS EC2`_
^^^^^^^^^^^

C'est une platforme de Cloud computing, EC2(Elastic Compute Cloud) est une service qui permet de déployer ce projet avec l'aide d'une instance (serveur virtuel hébergé dans EC2)

`CircleCI`
^^^^^^^^^^

Avec Circle CI/CD pipeline est fundamental component de ce projet pour un automatic developement et deployement.

Il aid a automatic test before merge, build et deploie une fois le projet est merger sur main.

Les environnement variables here_

.. note::

 Veuillez consulter plus d'informations de chaque logiciels, langages et technologies dans leur pages initiales.