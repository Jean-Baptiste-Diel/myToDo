# Image Python légère 
FROM python:3.10-slim 
# Dossier de travail dans le conteneur 
WORKDIR /app 
# Optimisation Python 
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 
# Copier les dépendances 
COPY requirements.txt . 
# Installer les dépendances 
RUN pip install --no-cache-dir -r requirements.txt 
# Copier tout le projet 
COPY . . 
# Port Flask 
EXPOSE 5000 
# Lancer l'application 
CMD ["python", "app.py"] 
