# Utiliser une image de base officielle Python 3
FROM python:3

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances et installer les packages nécessaires
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers du projet dans le conteneur
#COPY ./llm_qualitative_data_analysis .

# Définir la commande par défaut pour exécuter l'application
#CMD [ "python", "./your-script.py" ]
CMD ["tail", "-f", "/dev/null"]
