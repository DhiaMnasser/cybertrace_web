FROM python:3.6
LABEL maintainer="medazizknani@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV production
ENV DJANGO_SETTINGS_MODULE cybertrace.settings.production

COPY ./requirements.txt /code/requirements.txt

RUN apt-get update && apt-get install python3-mysqldb mysql-client dnsutils -y 
RUN pip install -r /code/requirements.txt
RUN pip install gunicorn

COPY . /code/
WORKDIR /code/

# RUN python manage.py makemigrations
# RUN python manage.py migrate

# RUN useradd wagtail
# RUN chown -R wagtail /code
# USER wagtail

EXPOSE 8000
CMD exec gunicorn cybertrace.wsgi:application --bind 0.0.0.0:8000 --workers 3 --access-logfile /var/log/web.access.log --error-logfile /var/log/web.error.log
