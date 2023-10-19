FROM python:3
#ENV VARIABLE SET DISABLE .PYC FILES vs no buffering infos   
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