# Agrégation de mathématques

## But de l'application

Le but de cette application est de fournir aux agrégatifs une interface leur permettant de préparer les épreuves orales et écrites de l'agrégation de matématiques.

### Préparation des leçons

Une application dédiée permet de de gérer, année par année, les leçons à préparer pour les oraux de ladite année. Chaque leçon comporte un titre et un numéro ainsi que les remarques du jury concernant la leçon.

Pour chaque leçon, chaque utilisateur peut écrire le plan en détail de ce qu'il compte présenter, des liens vers des développements (cf banque de développements) et vers des références (cf références). Il est possible de consulter (mais pas de modifier) le plan des autres utilisateurs.

### Banque de développments

L'application comporte une banque de développements rentrés par les utilisateurs. Avec chaque developpement vient des références pour le developpment.

### Références

Unr référence est simplement la donnée d'un titre, auteur, année de publication, etc. Il est aussi possible de joindre un fichier (.pdf par exmeple).

## Fonctionnalités

### Langage pour l'écriture du contenu

La quasi-intégralité du contenu (leçons, développements, commentaires, descriptions) est à rédiger par les utilisateurs selon les conventions markdown ([plus d'infos](https://fr.wikipedia.org/wiki/Markdown)) qui permettent, entre autre, d'inclure des mathématiques. Le texte est ensuite converti en html via l'outil `pandoc`.

### Autres fonctionnalités


