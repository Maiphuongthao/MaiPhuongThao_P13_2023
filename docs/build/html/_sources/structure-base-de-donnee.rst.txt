================================================================
Description de la structure de la base de données et des modèles
================================================================

.

Structure de la base de données
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _démarrer le serveur de développement Django: guide-de-demarrage-rapide.html

.. _la page d'administration: http://127.0.0.1:8000/admin/

Dans la carde ce projet Django, nous utilions la base de données relationnelles SQLite3.

La base de données SQLite3 est intégré directement dans Django ceque signifie que vous n'avez pas besoin d'installer un système de données externe.
Voici les 2 options pour accéder aux données du projets.

#. **L'interface d'administration de Django**:

Il lit automatiquement les metadatas des modèles et montre les données liées au x modèles. 
Il est conseillé d'utiliser cette interface pour organisation du management interne.
Pour accéder au interface, vous devez `démarrer le serveur de développement Django`_ et rendez vous sur `la page d'administration`_ dans votre navigateur web.

#. **SQLite3 shell**:

Dans votre terminal du projet, ouvrez SQLite3 shell avec la ligne de commande:

.. code-block::

    sqlite3

*Connecter à database du projet*:

.. code-block::

    .open oc-lettings-site.sqlite3

*Consulter les tables de database*:

.. code-block::

    .tables

*Consulter table colonnes*:
 
 example table : profiles_profile

.. code-block::

    pragma table_info(table);

*Consulter les informations d'une table*:

 example table : profiles_profile

.. code-block::

    select user_id, favarite_city from table where favarite_city like 'B%';

*Quittez SQLite3 shell*:

.. code-block::

    .quit

.

Modèles de données
^^^^^^^^^^^^^^^^^^^^

Les modèles de données est très importantes pour la structure de la base de données. Chaque modèle est associé à une table de base de données, les champs essentiels correspondent auw colonnes de la tabmes. Ils sont pour définier les données ainsi comment les données sont stockées et manipulées.


.. code-block:: python

    from django.db import models
    from django.contrib.auth.models import User


    class Profile(models.Model):
    """
    user=1 to many relation django auth user FK
    favorite_city =str
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username


En haut c'est une example de modèle de donnée **Profile** du projet. Les champs définissent sont **user** et **favorite_city**.

Dans cette modèle, le champs user a une relation avec la modèle User, il est déclaré par une clés étrangère.



