# Utiliser une image Node officielle
FROM node:18-alpine

# Dossier de travail
WORKDIR /app

# Copier tous les fichiers du projet dans le container
COPY . .

# Exécuter un fichier JavaScript au démarrage
CMD ["node", "bad-code.js"]
