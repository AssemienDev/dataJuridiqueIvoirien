# Projet de Modèle de Langage Juridique : Le Code Pénal Ivoirien

## Objectif

Ce projet a pour but de créer un modèle de langage pour comprendre et répondre à des questions liées au Code Pénal Ivoirien. Le modèle devra être capable de :

1. Répondre à des questions ouvertes sur le Code Pénal sans nécessairement utiliser un format strict, comme "Que dit l'article 1 ?".
2. Exploiter les informations du Code Pénal pour répondre à des demandes pratiques telles que : "Je suis dans un cas de délit de fuite, quelles sont les sanctions ?".

Nous utilisons deux types de modèles pour entraîner ce système :

- **Llama2** : Entraîné sur des données sous forme de questions et réponses (par exemple, "Que dit l'article 1 ?" et la réponse correspondante).
- **GPT-2** : Entraîné sur des données sous forme d'articles du Code Pénal avec leur contenu respectif (par exemple, "Article 1 : ...", puis le texte détaillé de l'article).

## Structure des données

Les données sont organisées de deux manières :

### 1. Llama2
Les données utilisées pour l'entraînement de Llama2 sont sous la forme suivante :

- **Question** : "Que dit l'article 1 ?"
- **Réponse** : Contenu détaillé de l'article 1.

L'objectif ici est que le modèle puisse répondre à des questions spécifiques concernant chaque article du Code Pénal.

### 2. GPT-2
Les données utilisées pour GPT-2 sont sous la forme suivante :

- **Article** : "Article 1"
- **Contenu** : Le texte intégral de l'article 1.

L'objectif pour GPT-2 est d'entraîner un modèle qui peut générer des descriptions détaillées des articles du Code Pénal en fonction du numéro d'article donné.

## Avancement du projet

Le projet est en cours d'entraînement avec deux modèles distincts :

1. **Llama2** : Le modèle est déjà bien avancé et nous avons commencé à entraîner le modèle sur les données de questions et réponses.
2. **GPT-2** : Le modèle est en phase d'entraînement sur les données du Code Pénal.

Nous avons déjà traité un certain nombre d'articles et de questions, et l'entraînement continue sur des serveurs dédiés avec des GPU puissants pour garantir une bonne performance.

## Contributeurs

Nous encourageons vivement les contributeurs à rejoindre ce projet et à aider à son développement. Voici quelques façons dont vous pouvez contribuer :

- Ajouter plus de données au dataset, notamment d'autres articles du Code Pénal (besoin).
- Tester les modèles et signaler les problèmes rencontrés (pas encore disponible).
- Proposer des améliorations pour augmenter la performance des modèles (pas encore disponible).
- Aider à la mise en production du modèle pour une utilisation réelle (pas encore disponible).

Si vous souhaitez contribuer, vous pouvez ouvrir une issue ou soumettre une pull request en faisant un fork du projet. Merci d'avance pour votre aide et votre soutien !

## Installation et utilisation

### Pré-requis

- Aucun pré-requis spécifique pour le moment, juste des données formatées selon les deux fichiers `jsonl`.

### Étapes

1. Récolter des données pour l'entraînement.
2. Formater les données pour l'entraînement selon soit code_penal_ivoirien_llama2 ou gpt2.
3. Partager sur ce repository.

## License

Ce projet est sous [la licence MIT](LICENSE).
