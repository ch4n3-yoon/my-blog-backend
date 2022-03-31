FROM python:3.8
ENV PYTHONUNBUFFERED 1

COPY ./ /code/
WORKDIR /code/

RUN pip install -r requirements.txt

RUN pip install uwsgi
#CMD uwsgi --ini uwsgi.ini
CMD python3 /code/manage.py runserver 0.0.0.0:3000

