# Agrégation de mathématiques

## But de l'application

Le but de cette application est de fournir aux agrégati-ve-f-s une interface leur permettant de préparer les épreuves orales et écrites de l'agrégation de mathématiques.

### Préparation des leçons

Une application dédiée permet de de gérer, année par année, les leçons à préparer pour les oraux de ladite année. Ce sont les templates de leçons : à savoir la donnée d'un titre et un numéro ainsi que les remarques du jury concernant la leçon et de savoir si la leçon est demandée à c-elles-eux qui préparent l'option informatique.

Pour chaque template de leçon, chaque utilisat-rice-eur peut écrire son plan en détail de ce qu'elle-il compte présenter, des liens vers des développements (cf banque de développements) et vers des références (cf références). Il est aussi possible de mettre des remarques personnelles pour chaque leçon, et de signaler lorsqu'une leçon est encore en cours d'écriture ou terminée. Il est possible de consulter (mais pas de modifier) le plan et les développements des autres utilisat-rice-eur-s.

Chaque utilisat-rice-eur à accès à une liste de (templates de) leçons qu'elle-il doit préparer (donc variable selon l'année et l'option qu'elle-il a choisi). Cette liste permet, en un coup d'oeil de connaître le leçons qu'elle-il lui reste à préparer, qui sont en cours de rédaction ou terminées et la quantité de développements pour chaque leçon.

### Banque de développements

L'application comporte une banque de développements rentrés par les utilisateurs. Avec chaque développement vient des références pour le développement. Il est possible de rédiger le développement en ligne (ce qui est idéal) ou simplement (ou dans un premier temps) de joindre un fichier (.pdf par exemple). Si le développement est rédigé en ligne, il est ensuite possible de l'exporter au format pdf ou LaTeX. Cela permet aussi de générer rapidement un document avec l'ensemble de tous ses développements.

Pour chaque leçon, un-e utilisat-rice-eur donne une liste de développements avec, si elle-il le souhaite, des remarques personnelles pour chaque développement (ex: à quoi faire attention, etc.).

### Références

Une référence est simplement la donnée d'un titre, auteur, année de publication, etc. Il est aussi possible de joindre un fichier (.pdf par exemple). Les références sont appelées par des leçons ou des développements. Il est possible d'obtenir une liste des références auxquelles ses leçons et développement font appel.

## Fonctionnalités

### Langage pour l'écriture du contenu

La quasi-intégralité du contenu (leçons, développements, commentaires, descriptions) qui est à rédiger par les utilisat-rice-eur-s est à écrire au format markdown ([plus d'infos](https://fr.wikipedia.org/wiki/Markdown)). Il s'agit d'un langage de balisage extrêmement simple et qui permettent, entre autre, d'inclure des mathématiques. Le texte est ensuite converti en html via l'outil `pandoc`. Chaque utilisat-rice-eur peut avoir un préambule LaTeX personnalisé pour y définir ses macros ou ses choix de style.

### Autres fonctionnalités

* Il est possible d'exporter la plus part du contenu (leçons, développements, etc.)  au format .pdf ou .tex pour pouvoir le réutiliser ailleurs ou l'imprimer.
