=======================================
Procédures de déploiement et de gestion
=======================================

.

.. _les langages et technologies: technologies-et-langages.html

.. _projet clôné: installation.html

.. _l'environnement virtuel: guide-de-demarrage-rapide.html


.. note::

    Les installations sont nécessaires:

    - `les langages et technologies`_ du projet.

    - `projet clôné`_ dans votre ordinateur

    - `l'environnement virtuel`_ , le requirements.txt et .env installés

.

Dockerfile et docker-compose
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nous avons un fichier Dockerfile avec les instructions pour la création une image docker.


.. code-block::

    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1
    #create work directory
    RUN mkdir /code
    WORKDIR /code
    #copy requirement to be install
    COPY requirements.txt /code/
    RUN pip install -r requirements.txt
    #copy project
    COPY . /code/
    # Collect static files
    ARG SECRET_KEY 
    ARG SENTRY_DSN 
    ARG DEBUG 
    # ENV DEBUG ${DEBUG}
    EXPOSE 80
    RUN python manage.py collectstatic --noinput
    CMD gunicorn oc_lettings_site.wsgi --log-level debug -b 0.0.0.0:80

docker-compose.yml permets de lancer l'image plus facile, et si vous avez plusieur conteneurs.

.. code-block::

    version: '3'

    services:
    web:
        image: maiphuongthao/oc-lettings:latest
        ports:
        - "80:80"

.


AWS ec2
^^^^^^^

* Créer un compte de AWS puis créer une `instance AWS EC2`_.

.. _instance AWS EC2: https://www.techtarget.com/searchcloudcomputing/tutorial/How-to-create-an-EC2-instance-from-AWS-Console

* `Installer Docker`_ et docker-compose à l'instance.

.. _Installer Docker: https://www.learnitguide.net/2023/04/how-to-install-docker-on-ubuntu.html

* Récupèrer `AWS_ACCESS_KEY_ID et AWS_SECRET_ACCESS_KEY`_.

.. _AWS_ACCESS_KEY_ID et AWS_SECRET_ACCESS_KEY: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html

.

Circle CI/CMD
^^^^^^^^^^^^^

Si vous n'avez pas encore un compte de CircleCI, vous pouvez vous s'inscrire ici_.

.. _ici: https://circleci.com/vcs-authorize/

.. _projet: https://circleci.com/docs/getting-started/

.. _connecter: https://circleci.com/blog/setting-up-continuous-integration-with-github/

.. _Ajouter environnement variables: https://circleci.com/docs/set-environment-variable/

Créer un nouveau projet_ ou connecter_ le projet forké de votre GitHub à Circle CI.
Remplacer le répertoire .circleci avec celui du projet.

`Ajouter environnement variables`_ dans votre projet de circleCI:

.. list-table::
   :widths: 30, 70
   :header-rows: 1

   * - Key
     - Value
   * - DOCKER_LOGIN 
     - Docker Hub Id
   * - DOCKER_PASSWORD 
     - Docker Hub password
   * - DEBUG
     - False 
   * - SECRET_KEY 
     - Django secret key
   * - SENTRY_DSN
     - Sentry DSN 
   * - AWS_ACCESS_KEY_ID 
     - AWS access key id 
   * - AWS_SECRET_ACCESS_KEY
     - AWS secret key of access key  
   * - AWS_DEFAULT_REGION
     - aws default region 
   * - SG_ID row 9
     - sg of aws ec2 instance security group 
   * - SSH_HOST row
     - aws ec2 instance IP public or DNS public 
   * - SSH_USER row
     - aws ec2 instance user
     
     
Une pipeline Circle CI/CD qui est crée. Créer une branch en parallèle avec votre branch master, avec cette configuration, vous pouvez:

**Compliation**: *Lancer les tests après chaque commit*

.. code-block::

    jobs:
        testing:
            docker:
            - image: cimg/python:3.8
                environment:
                SECRET_KEY: $SECRET_KEY
                SENTRY_DSN: $SENTRY_DSN
                DEBUG: $DEBUG
            steps:
            - checkout
            - run:
                name: install dependencies
                command: |
                    python3 -m venv env
                    source env/bin/activate
                    pip install -r requirements.txt
            - run:
                name: launch test
                command: |
                    source env/bin/activate
                    flake8
                    pytest --cov
                    echo "TESTING COMMIT $CIRCLE_SHA1"
            
**Contrainerisation**: *Créer image docker and pousser sur Docker Hub*

.. code-block::

    publish_docker:
        docker:
        - image: cimg/python:3.9
            environment:
            SECRET_KEY: $SECRET_KEY
            SENTRY_DSN: $SENTRY_DSN
            DEBUG: $DEBUG
        steps:
        - checkout
        - setup_remote_docker:
            version: 20.10.12
        - run:
            name: Build and publish Docker image
            command: |
                docker login -u $DOCKER_LOGIN -p $DOCKER_PASSWORD
                docker build -t $DOCKER_LOGIN/oc-lettings:latest -t $DOCKER_LOGIN/oc-lettings:$CIRCLE_SHA1 \
                --build-arg SECRET_KEY=$SECRET_KEY \
                --build-arg SENTRY_DSN=$SENTRY_DSN \
                --build-arg DEBUG=$DEBUG \
                .
                docker push --all-tags $DOCKER_LOGIN/oc-lettings

     
**Deployment**: *Installer AWS Cli, ajouter circleci dans security group, add docker-compose file et lance Docker image sur instance"

.. code-block::

    deploy_to_aws:
        docker:
        - image: cimg/python:3.8
        steps:
        - checkout
        - run:
            name: install dependencies
            command: |
                python3 -m venv env
                source env/bin/activate
        - run:
            name: Test deploy 
            command: |
                # echo "$SSH_KEY" >> /tmp/deploy_key
                # chmod 600 /tmp/deploy_key

                # 1- Install AWS CLI
                source env/bin/activate
                curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
                unzip awscli-bundle.zip
                ./awscli-bundle/install -b ~/bin/aws
                echo "2- Get the public IP of the current CircleCI runner"
                PUBLIC_IP=$(curl ipinfo.io/ip)
                echo " 5- Add an ingress rule to the security group"
                echo "region: $AWS_DEFAULT_REGION"
                ~/bin/aws ec2 authorize-security-group-ingress --region $AWS_DEFAULT_REGION --group-id $SG_ID \
                --protocol tcp --port 22 --cidr $PUBLIC_IP/24
                echo "6- Give the ingress rule some time to propagate"
                sleep 5
                # ssh -o StrictHostKeyChecking=no $SSH_USER@$SSH_HOST "mkdir -p ./code"
                scp -o StrictHostKeyChecking=no ./docker-compose.yml $SSH_USER@$SSH_HOST:/home/ubuntu
                echo "connecting to instance"
                ssh -o StrictHostKeyChecking=no $SSH_USER@$SSH_HOST "docker login -u $DOCKER_LOGIN -p '${DOCKER_PASSWORD}' && docker-compose pull && docker-compose -f /home/ubuntu/docker-compose.yml up -d"
                echo "docker stuff"
                # 8- Remove the ingress rule
                ~/bin/aws ec2 revoke-security-group-ingress --region $AWS_DEFAULT_REGION --group-id $SG_ID \
                --protocol tcp --port 22 --cidr $PUBLIC_IP/24
     
     
     
     
