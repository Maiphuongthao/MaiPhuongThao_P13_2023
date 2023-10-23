![](static/assets/img/circleci-icon.svg)
<p align="center">
  <a href="https://www.python.org/">
    <img src="https://skillicons.dev/icons?i=python" />
  </a>
  <a href="https://www.djangoproject.com/">
    <img src="https://skillicons.dev/icons?i=django" />
  </a>
  <a href="https://getbootstrap.com/">
    <img src="https://skillicons.dev/icons?i=bootstrap" />
  </a>
  <a href="https://www.w3schools.com/css/">
    <img src="https://skillicons.dev/icons?i=css" />
  </a>
  <a href="https://docs.sentry.io/">
    <img src="https://skillicons.dev/icons?i=sentry" />
  </a>
  <a href="https://www.docker.com/">
    <img src="https://skillicons.dev/icons?i=docker" />
  </a>
  <a href="https://circleci.com/docs/jobs-steps/">
    <img width="48" height="48" src="https://img.icons8.com/color/48/circleci.png" alt="circleci"/>
  </a>
  <a href="https://aws.amazon.com/fr/ec2/">
    <img src="https://skillicons.dev/icons?i=aws" />
  </a>
  <a href="https://www.sqlite.org/index.html">
    <img src="https://skillicons.dev/icons?i=sqlite" />
  </a> 
</p>



## Menu   
1. **[General informations](#general-informations)**
2. **[Prerequisite list](#list-of-prerequisites)**    
2. **[Documentation Read the Docs](#documentation)**   
3. **[Fonctionnalitées](#fonctionnalitées)**   
4. **[Interface d'administration Django](#interface-administration-django)**   
  
6. **[Tests et couverture de code](#tests-et-couverture-de-code)**   
7. **[Création environnement](#creation-environnement)**   
8. **[Activation environnement](#activation-environnement)**   
9. **[Installation des librairies](#installation-librairies)**   
10. **[Exécution de l'application](#execution-application)**   
11. **[Rapport avec flake8](#rapport-flake8)**   
12. **[Informations importantes sur les différents fichiers et dossiers](#informations-importantes)**   
13. **[Auteur et contact](#auteur-contact)**  

--------------------------------------------------------------------------------------------------------------------------------

<div id="general-informations"></div>

### General informations

Orange County Lettings is a start-up real estate company in the US.
The but is to improve the base code from their github [Python-OC-lettings_FR](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR), then to the deployment.

Basic demands:

__Technical aspects__

- Organise the project to 2 diffirents apps: lettings & profiles to improve the modular architecture
- Fill the new tables with informations of old tables by using Django migrations
- Organise correct templates files to correct apps 
- Rename request html templates
- Clear all unecessary files from project folder

__Reduce several diver problems__

- Several reported linting errors need to be fixed. Do not change the information from setup.cfg
- Django admin shows error for Address model , plural version
- Create 404 and 500 pafe to ensure when there is needed
- Correct docstring comments
- Create tests for projects and apps with coverage >=80%

__Monitoring and tracking errors with Sentry__

- Build un monitoring system by using Sentry
- Build logging to project to survey the errors

__Pipeline CI/CD wtih [CircleCI](https://circleci.com/docs/jobs-steps/) and deploy the project to [AWS EC2](https://aws.amazon.com/fr/ec2/) instance__

- *Compilation*: Test the linting and project tests
- *Containerisation*: Build and push image with [Docker and Docker-compose](https://skillicons.dev/icons?i=docker)
- *Deployment*: Deploy the site to AWS EC2

--------------------------------------------------------------------------------------------------------------------------------

<div id="list-of-prerequisites"></div>





## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`
