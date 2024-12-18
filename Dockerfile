FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
WORKDIR /app
COPY . /app/

# En cas de virtuel
#RUN python3 -m venv /env

ENV PATH="/env/bin/$PATH"

# Ajouter le fichier shell
COPY entrypoint.sh /app/entrypoint.sh

RUN python3 -m pip install --upgrade pip

#Install Django and other required packages
RUN pip install django

COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
