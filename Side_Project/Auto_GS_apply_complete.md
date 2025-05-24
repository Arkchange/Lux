**Idée** : Besoin d'un macro pour eviter de tout le temps compléteer mes suivie de candidatures a la main apres candidature
Je suppose que pour chaque candidature faites, la données est entreé dans la sheet.

→ Développement d'une macro sur Google sheet qui permet une automatisation des réponses sur les candidatures recu par mails.

Cette automatisation prend en compte :
- Le poste
- La date de candidature
- L'entreprise
- Statue de la candidature ( "Refus", "en cours", "pris, ou "")

Le déroulement se passe comme ceci : 
- Toutes les n instances de temps, la macro va s'activer et regarder mes mails sur un intervalle de 7 jours
- Pour chaque mails recu, il scan l'objet, l'expediteur, le corps du mail et me donne si on a un **match**, une note entre "refus", "en cours", ou "pris"
- Elle parcourt ensuite pour le meme poste et meme entreprise la sheet et regarde si le statue est vide ("") ou non. Si c'est le cas, il met la note sur la cellule statue.
- Si l'entreprise, le poste et le statue remplisse toutes les conditions et que c'est la seul ligne, il attribut directement la note dans la cellule. Sinon, elle prend celle qui a la date la moins récentes
- En parcourant les mails, après les avoir lus, il attribue un label sur Gmail comme "CandidatureVu" ce qui empêche une rebondance des mail vu.
- Pour des questions de CI/CD, création d'une page log afin de voir le comportement de la macro
