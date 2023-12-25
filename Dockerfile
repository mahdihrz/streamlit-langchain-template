# Utiliser une image de base officielle Python 3
FROM python:3

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances et installer les packages nécessaires
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Définir la commande par défaut pour exécuter l'application
#CMD [ "python", "./your-script.py" ]
CMD ["tail", "-f", "/dev/null"]
