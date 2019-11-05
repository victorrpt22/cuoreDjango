FROM python:3.8
COPY ./ /home/hospital
WORKDIR /home/hospital
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

CMD ./entrypoint.sh



python manage.py runserver 0.0.0.0:8000
