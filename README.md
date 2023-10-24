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



# Menu   
1. **[General informations](#general-informations)**
2. **[Prerequisite list](#list-of-prerequisites)**
3. **[Installation](#installation)**
4. **[Development the site locally](#launch-locally)**       
2. **[Admin](#admin)**   
3. **[Production](#production)**   
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

## General informations

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

## Prerequisite list

- Compte GitHub with reading access to this repository
- Git CLI
- SQLite3 CLI
- Python 3.6 or higher
- Django 3.0
- Docker 24.0
- Docker-compose 2.22.0
- AWS CE2
- Sentry

--------------------------------------------------------------------------------------------------------------------------------

<div id="installation"></div>

## Installation

#### Clone the repository

- `git clone https://github.com/Maiphuongthao/MaiPhuongThao_P13_2023.git`
- `cd MaiPhuongThao_P13_2023`

#### Create variable environnement and install the requirements

- The programme uses multiples modules and libraries which are noted in requirements.txt to be installed.
- It's recommended to create the variable environnement to install any module

Windows :

   ```
    
    python -m venv env 
    env\scripts\activate

    pip install -r requirements.txt

  ```

MacOS et Linux :

  ```
    
    python3 -m venv env 
    source env/bin/activate

    pip install -r requirements.txt

  ```

#### Protect the secret informations

- `touch .env` to create an env file
- In side the .env file copy and add values to three variables that you found in .evn.example

--------------------------------------------------------------------------------------------------------------------------------

<div id="launch-locally"></div>

## Development the site locally

- `cd MaiPhuongThao_P13_2023`
- `source venv/bin/activate`

#### launch the site

__Without docker__

- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.

__With docker__

- You will need to install docker and docker-compose locally, following [here](https://www.docker.com/get-started/)

- `docker-compose down`
- `docker-compose-up -d`

#### Have a look at the tests and tests'scoverage

- `pytest`
- `pytest --cov`

#### Linting

- `flake8`

#### Database

- `sqlite3` to open sqlite3 shell
- `.open oc-lettings-site.sqlite3` to connect to database
- `.tables` to show tables in db 
- `pragma table_info(profiles_profile);` to show profile's columns 
- `select user_id, favorite_city from profiles_profile where favorite_city like 'B%';`to launch a request to profile table, 
- `.quit` to quit the shell

--------------------------------------------------------------------------------------------------------------------------------

<div id="installation"></div>

## Admin

- Connect to `http://localhost:8000/admin` page
- User`admin`, mot de passe `Abc1234!`

--------------------------------------------------------------------------------------------------------------------------------

<div id="installation"></div>

## Production

- This project is made in production mode so there is alread .circleci folder and config.yml file

#### Setup AWS EC2

- Create an AWS account and an EC2 instance by following [here](https://www.techtarget.com/searchcloudcomputing/tutorial/How-to-create-an-EC2-instance-from-AWS-Console)
- Connect to instance then install docker and docker-compose [here](https://www.learnitguide.net/2023/04/how-to-install-docker-on-ubuntu.html)
- create access key id and secret key by following [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)

#### Setup CircleCI/CD

- Create an account circleci then connect to this project via githup, following instruction [here](https://www.digitalocean.com/community/tutorials/how-to-automate-deployment-using-circleci-and-github-on-ubuntu-18-04)

- Remember to use the circle folder and config.yml file of the project
- Add environnement variables, following instruction [here](https://circleci.com/docs/set-environment-variable/):

| Key                | Value                         |
|---------------------|--------------------------------|
| DOCKER_LOGIN        | Docker Hub Id   |
| DOCKER_PASSWORD     | Docker Hub password  |
| DEBUG      | False       |
| SECRET_KEY          | Django secret key        |
| SENTRY_DSN          | Sentry DSN              |
| AWS_ACCESS_KEY_ID          | AWS access key id               |
| AWS_SECRET_ACCESS_KEY   | AWS secret key of access key               |
| AWS_DEFAULT_REGION  | aws default region        |
| SG_ID          | sg of aws ec2 instance security group                 |
| SSH_HOST          | aws ec2 instance IP public or DNS public      |
| SSH_USER          | aws ec2 instance user               |

#### Deployment

This project is using Trunk-base development as a version control management practice: one master branch, one development branch & Circleci pipeline

- Testing:  After each commit on addition branch ( developement or else), the tests will be executed automatically
- Build image: When the tests are passed and the branch is merged to master, docker contener and image will be created then sent to Docker Hub
- Deploy: aws will be installed with circleci, then it will add circleci ingress to security group, then connect to aws ec2 instance, from there the docker which is installed in the instance will copy docker-compose file then search for latest image to deploy

Here we have the website fully deployed to an ip public.