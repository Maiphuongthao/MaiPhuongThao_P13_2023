======================
Description du Projet
======================

Orange County Lettings est un start-up dans le secteur de la location de bien immobiliers. La start-up est en pleine phase d'expansion aux Etats-Unis.

.. image:: _static/lettings.png


Nous entreprenons la démache d'amélioration de notre siteweb actuel. Les objectifs principals sont de:

Amélioration de l'architecture modulaire
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nous optimisons notre architecture de site web en résuisant les problèmes de notre conception ùonolitique actuelle. Nous allons:
 * Réorganiser notre code en plusieurs applications distinctes
 * déplacer les fichiers HTML du site dans des dossiers de templates spécifiques à chaque application.

Cette optimisation améliorera la flexibilité, la maintenabilité et l'évolutivité de notre code.


Réduction de divers problèmes sur le projet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plusieurs problèmes à résoudre dans l'application:
 * Corriger les erreurs de linting sans toucher à setup.cfg
 * Corrier l'erreur de pluralisation pour le terme "adresse" dans la section d'administration
 * Ajouter les pages 404 et 500
 * Correcter les docstrings
 * Mettre en places les tests et maintenir la couverture des test à plus de 80%


Surveillance de l'application et suivi des erreur via Sentry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dans le cadre de l'optimisation de notre application, nous souhaitons mettre en place un système de surveillance et de gestion des erreurs plus robuste en utilisant Sentry et logging.