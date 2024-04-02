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

COPY requirements.txt /app/
RUN pip install -r requirements.txt
