FROM python:3.12
# Installer les dépendances nécessaires pour pyaudio
RUN apt-get update && apt-get install -y portaudio19-dev python3-dev libffi-dev libssl-dev ffmpeg && rm -rf /var/lib/apt/lists/*

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

#Exposer le port sur lequel il va tourner
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
