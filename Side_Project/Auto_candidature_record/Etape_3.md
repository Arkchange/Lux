**Idée** : Besoin d’une macro pour éviter de compléter manuellement le suivi de mes candidatures à chaque fois.
Je pars du principe que, pour chaque candidature envoyée, les données sont saisies dans la Google Sheet.

→ Développement d’une macro sur Google Sheets permettant d’automatiser la mise à jour des réponses reçues par mail suite aux candidatures.
Cette automatisation prend en compte :
- Le poste
- La date de candidature
- L'entreprise
- Le statut de la candidature ("Refus", "En cours", "Pris", ou vide "")

Le déroulement se passe comme ceci : 
- Toutes les _n_ unités de temps, la macro s’active et analyse mes mails sur un intervalle de 7 jours.
- Pour chaque mail reçu, elle scanne l’objet, l’expéditeur, et le corps du mail, et détermine s’il y a un match. Elle attribue alors une note parmi "Refus", "En cours", ou "Pris".
- Elle parcourt ensuite la Google Sheet pour retrouver, pour le même poste et la même entreprise, les lignes où la cellule "statut" est vide. Si c’est le cas, elle y inscrit la note correspondante.
- Si l’entreprise, le poste et le statut remplissent toutes les conditions et qu’il n’y a qu’une seule ligne correspondante, elle attribue directement la note. Sinon, elle choisit celle avec la date de candidature la plus ancienne.
- Après lecture, chaque mail est étiqueté dans Gmail avec un label (par exemple : "CandidatureVu") afin d’éviter qu’il ne soit traité plusieurs fois.
- Par souci de traçabilité (CI/CD), une feuille de logs est créée afin de suivre le comportement de la macro.

Résultat avant : ![image](https://github.com/user-attachments/assets/e42a231a-5315-4ab2-b5c1-9cf1f9ead631)

Résultat après : ![image](https://github.com/user-attachments/assets/f9f353dc-c9fb-43b3-9d3f-4e8f0b38c7e3)

Avec les logs : ![image](https://github.com/user-attachments/assets/c685a3e2-4252-43b1-b793-74d2a6c8e18a)

**Problème identifié** : Pour le poste Infiltré, le mail mentionne "d'Infiltré", ce qui, après nettoyage, devient dinfiltré. Cela empêche une correspondance exacte avec le poste attendu, car le mot est fusionné avec la préposition.

**Solution à envisager** : Mettre en place un traitement spécifique dans la fonction de nettoyage pour supprimer les prépositions contractées (comme "d'", "l'", "qu'") lorsqu'elles précèdent un mot, afin d'améliorer la robustesse de la macro.


