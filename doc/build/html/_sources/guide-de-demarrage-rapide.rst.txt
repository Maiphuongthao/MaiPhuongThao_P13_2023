=========================
Guide de démarrage rapide
=========================

.. note::

    *Requirement:*
    
    - GitHub & projet forké et clôné dans votre machine local
    - Docker
    - Sentry - DSN
    - SECRET_KEY de Django projet
    - DEBUG - True pour developpement ou False pour Production

.

Démarrage avec le terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::

    Il est conseillé d'éviter d'installer les modules, packages supplémentaires du projet directement dans votre base. C'est un bon habitude d'utiliser un environnement virtuel.


1. **Envirennement virtuel**

Ce projet est créée avec langage Python, vous devez installer une version Python_ compatible pour votre ordinateur.

.. _Python: technologies-et-langages.html

Dans le terminal de racine du projet, créer votre répertoire de environnement puis l'activer:


*Window*:

.. code-block::

    python -m venv env
    env\scripts\activate

    pip install -r requirements.txt


*MacOS et Linux*:

.. code-block::

    python -m venv env
    source env/bin/activate

    pip install -r requirements.txt 


*Déactivate l'environnement virtuel si besoin*: 

.. code-block::

    deactivate


2. **Créer un fichier .env pour les informations secrets**

*Dans le termnal du répertoire principal:*

.. code-block::

    touch .env


*Ajouter ces information dans le fichier:*

 SENTRY_DSN = "Votre DSN de Sentry"

 SECRET_KEY = "Votre django secret key"

 DEBUG = "False" - ou True pour dévéloppement local


Les informations dans .env ne va pas être partagé.


3. **Lancer le projet avec la commande**

*Dans le terminal de racine du projet, tapez*:

.. code-block::
    
 python manage.py runserver

Le projet vont va être lancé sur le localhost: 8000, à l'adresse : http://127.0.0.1:8000/

.

Démarrage avec Docker
^^^^^^^^^^^^^^^^^^^^^

.. warning::
    
    Il est necessaire que Docker_ et Docker-compose installés dans votre ordinateurs.

.. _Docker: technologies-et-langages.html

1. **Cas 1**

Projet est clôné, l'environnement virtuel et installation des packages, modules sont terminée. 
Vous pouvez lancer les commandes suivantes dans votre terminal:

Nettoyer les resources deployées avec

.. code-block::

    docker-compose down

Lancer le projet

.. code-block::

    docker-compose up -d

 


2. **Cas 2**

Si vous n'avez pas le projet installé dans votre ordinateur.

Dans votre terminal, lancez la commande:

.. code-block::

    docker run --publish 0.0.0.0:80:80 --name nomdeconteneur -it maiphuongthao/oc-lettings


Cette commande va chercher automatiquement sur réseau docker image qui contient le projet, la mettre dans un conteneur "nomdeconteneur" puis la lancer au port 80.


