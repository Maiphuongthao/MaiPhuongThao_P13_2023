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
RUN python manage.py collectstatic --noinput
CMD python3 manage.py runserver 0.0.0.0:8000