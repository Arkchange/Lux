Révision de : 

https://pythonds.linogaliana.fr/content/NLP/03_embedding.html

Avant d'approcher une base de données contenant des textes, il faut au préalable les nettoyer en enlevant la ponctuation et les stopwords. Ensuite, il faut encoder les features catégoriques et splitter les données en 80\% d'entraînement et 20\% de test.

Pour trouver le texte le plus similaire :

Il présente une approche BoW qui utilise le **TF-IDF** sur tout le corpus et applique une similarité cosinus entre le texte vectorisé et le corpus, ce qui permet de renvoyer les textes du corpus les plus similaires au texte donné.

Une autre approche consiste à utiliser **LangChain**, où l’on applique également le **TF-IDF** sur tout le corpus (agissant comme un retriever) et qu’on stocke dans une base de données vectorielle. Ensuite, à partir d’un texte donné, on cherche sa contrepartie la plus proche dans cette base vectorielle, ce qui mène à un résultat similaire.

Mais ces méthodes ont des faiblesses : par exemple, le mot Frankenstein est assez rare et devrait favoriser un auteur en particulier, mais on ne voit pas ce résultat de façon évidente.

Il mentionne aussi la possibilité de faire une classification à partir du texte pour identifier l’auteur qui l’a écrit.

On rencontre alors un problème pour les corpus à grande échelle, où la vectorisation prendra un espace énorme, avec beaucoup de zéros si les mots ne sont pas présents, donc une représentation peu dense. Cette observation s'accompagne d’une baisse en efficacité de l’approche. Ce que l’on veut, c’est une représentation dense afin de mieux généraliser l’information. C’est là qu’intervient **Word2Vec**, l’ancêtre des LLM.

Ce modèle résout une limite du BoW en créant des features, comme vu au Day 1. Par exemple, si un document porte sur les rois et un autre sur les reines, un humain perçoit naturellement une similarité. Un modèle bien entraîné pourra identifier une feature de **royauté**, voire aller plus loin en créant une feature de genre dans un espace sémantique où les relations sont algébriquement logiques :

$$King - man + woman \approx queen$$
$$Paris - France + Italy \approx Rome$$

Ces analogies fonctionnent aussi entre différentes langues, comme un système de transfert, tout cela grâce à la similarité des mots.

Pour que cela fonctionne, les modèles sont entraînés avec des réseaux de neurones. L’idée est que chaque mot est défini par son entourage, et le but est de prédire l’entourage à partir du mot (ou inversement). En répétant ce processus sur un large corpus, on obtient des embeddings.

Il existe deux approches principales :
- prédire le mot à partir du contexte → **CBOW** (_Continuous Bag of Words_)
- prédire le contexte à partir du mot → **Skip-gram**



