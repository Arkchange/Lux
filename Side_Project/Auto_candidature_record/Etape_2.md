**Idée** : En supposant que l'étape post-candidature est totalement automatisée, je vais chercher à automatiser les étapes intermédiaires pour compléter le journal.

Pour cela, j'ai créé 3 macros qui remplissent le journal à partir des données supposées renseignées.

- La première macro consiste à entrer un lien (https:) dans la colonne "Lien", qui va automatiquement se transformer en hyperlien avec le texte Lien. Cette transformation est nécessaire pour conserver un journal de taille équilibrée et lisible. Cette étape ne pourra pas être automatique et est optionnel.

- La deuxième macro permet, dès qu’une nouvelle ligne est ajoutée, de drag down automatiquement toutes les colonnes dépendantes d'autres facteurs (ex. : Date, Statut), ce qui permet de compléter le journal par des calculs automatiques.

- La troisième macro est, selon moi, optionnelle. Elle prend une date au format ddmmyyyy et la transforme en format date dd/mm/yyyy, en prenant en compte le cas où le jour commence par un zéro (ex. : 07022024 devient 7022024, ce que Google Sheets ne reconnaît pas automatiquement comme une date valide). Cette macro dépendra de la facilité avec laquelle je pourrai scraper les données de date, que ce soit au format dd/mm/yyyy ou ddmmyyyy.




