Révision de ces 3 liens sur le NLP

https://pythonds.linogaliana.fr/content/NLP/
https://pythonds.linogaliana.fr/content/NLP/01_intro.html
https://pythonds.linogaliana.fr/content/NLP/02_exoclean.html

Ce qui est mentionnée : 
- Utilisation des packages NLTK et SpaCy pour travailler sur des données non structurées afin de les analyser.
- Deux méthodes qui peuvent réduire le temps d'exécution du code sont la lemmatisation et la racination. Toutes deux ont leurs avantages et inconvénients.

**Lemmetisation** : Transforme les mots au pluriel ou conjugués en leur forme simple (chevaux devient cheval, etc.) dans le but d’harmoniser les termes.
**Racination** : Transforme les mots en leur forme racine (cheval devient chev, mais chevet aussi).

La méthode TF-IDF (_Term Frequency-Inverse Document Frequency_) calcule un score de proximité entre un terme et un document. Elle est majoritairement utilisée par les moteurs de recherche afin d’évaluer la pertinence des documents.

$$TFIDF(i,d,D) = TF(t,d) * IDF(t,D)$$

où **t** est le terme, **d** le document et **D** le corpus. **TF** calcule ne nombre d'occurence de t dans d et **IDF** est défini comme : $$log(\frac{N}{|{d \in D|t \in d}|})$$

où **N** nombre de total de documents dans D, et l'ensemble $|{d \in D \mid t \in d}|$ représente le nombre de documents contenant le terme t.

Les faiblesses des méthodes "**bag of words**" résident dans **l'absence de contexte** et dans la représentation dite sparse, qui rend le rapprochement entre les mots et leur contexte moins pertinent.
Pour briser ces limites, on introduit les n-grams, qui consistent à créer des liens entre les tokens (considérés comme indépendants dans la méthode classique). Cette approche s'intéresse non seulement aux mots et à leur fréquence, mais aussi aux mots qui les suivent. Il est généralement préférable d'utiliser les bigrams ou les trigrams, car plus on augmente la valeur de n, plus l'espace de stockage requis augmente, ce qui peut entraîner une baisse de performance.

Ils introduisent également **FastText** (_un sac de n-grams_), qui est un modèle de réseau de neurones destiné à la classification de texte (déterminer sa catégorie d’appartenance). Il transforme des données non structurées en données structurées en créant des features à partir de groupements de texte (capture la notion de contexte). FastText est souvent utilisé pour classifier rapidement et avec précision des e-mails, articles, tweets, etc.



