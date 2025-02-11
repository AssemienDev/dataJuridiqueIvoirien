# Projet de Modèle de Langage Juridique : Le Code Pénal Ivoirien

## Objectif

Ce projet a pour but de créer un modèle de langage pour comprendre et répondre à des questions liées au Code Pénal Ivoirien. Le modèle devra être capable de :

1. Répondre à des questions ouvertes sur le Code Pénal sans nécessairement utiliser un format strict, comme "Que dit l'article 1 ?".
2. Exploiter les informations du Code Pénal pour répondre à des demandes pratiques telles que : "Je suis dans un cas de délit de fuite, quelles sont les sanctions ?".

Nous utilisons deux types de modèles pour entraîner ce système :

- **T5-small** : Entraîné sur des données sous forme de questions et réponses (par exemple, "Que dit l'article 1 ?" et la réponse correspondante).
- **GPT-2** : Entraîné sur des données sous forme d'articles du Code Pénal avec leur contenu respectif (par exemple, "Article 1 : ...", puis le texte détaillé de l'article).

## Structure des données

Les données sont organisées de deux manières :

### 1. T5-small
Les données utilisées pour l'entraînement de T5-small sont sous la forme suivante :

- **Entrée** : "question: Que dit l'article 1 ? context: Article 1 [texte détaillé de l'article]"
- **Sortie** : Contenu détaillé de l'article 1.

L'objectif ici est que le modèle puisse répondre à des questions spécifiques concernant chaque article du Code Pénal.

### 2. GPT-2
Les données utilisées pour GPT-2 sont sous la forme suivante :

- **Article** : "Article 1"
- **Contenu** : Le texte intégral de l'article 1.

L'objectif pour GPT-2 est d'entraîner un modèle qui peut générer des descriptions détaillées des articles du Code Pénal en fonction du numéro d'article donné.

## Avancement du projet

Le projet est en cours d'entraînement avec deux modèles distincts :

1. **T5-small** : Le modèle est déjà bien avancé et nous avons commencé à entraîner le modèle sur les données de questions et réponses. \
[t5_codepenal]( https://huggingface.co/AssemienDev/t5_codepenal)
2. **GPT-2** : Le modèle est en phase d'entraînement sur les données du Code Pénal. \
[gpt2_codepenal](https://huggingface.co/AssemienDev/gpt2_codepenal)

Nous avons déjà traité un certain nombre d'articles et de questions, et l'entraînement continue sur des serveurs dédiés avec des GPU pas trop puissants gratuit pour garantir une performance.

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
2. Formater les données pour l'entraînement selon soit `legalbert_dataset` ou `code_penal_gpt2`.
3. Partager sur ce repository.

## Tests du modèle t5_codepenal
Voici la section mise à jour pour inclure les instructions concernant l'utilisation de Google Colab pour tester le modèle `t5_codepenal` :

---

## Tests du modèle t5_codepenal

Pour tester le modèle `t5_codepenal`, voici les étapes à suivre :

### 1. Cloner le repository

Commencez par cloner ce repository sur votre machine locale ou sur une plateforme de développement comme Google Colab. Vous pouvez cloner le repo avec la commande suivante :

```bash
git clone https://github.com/AssemienDev/dataJuridiqueIvoirient.git
cd dataJuridiqueIvoirien
```

### 2. Lancer les tests sur une machine avec un puissant CPU ou GPU

Pour une exécution optimale, il est recommandé d'exécuter les tests sur une machine avec un **GPU puissant**. Si vous n'avez pas accès à une telle machine, vous pouvez utiliser **Google Colab**, une plateforme gratuite qui vous permet d'exécuter des modèles de machine learning avec un GPU.

#### Utilisation de Google Colab

Voici comment vous pouvez configurer et tester le modèle sur Google Colab :

1. Ouvrez un nouveau notebook sur [Google Colab](https://colab.research.google.com/).
2. Clonez le repository dans votre notebook en exécutant la commande suivante :

```python
!https://github.com/AssemienDev/dataJuridiqueIvoirien.git
%cd dataJuridiqueIvoirien
```

3. Installez les dépendances nécessaires pour exécuter le modèle. Exécutez les commandes suivantes :

```python
!pip install torch transformers datasets
```

4. Exécuter le fichier [testeurModeleT5CodePenal.py](t5_codepenal%2FtesteurModeleT5CodePenal.py) :

```python
question_to_ask = "Quel est le contenu de l'Article 1 ?"
```
Changer le chiffre de l'article pour tester de 1 à 502.

5. Une fois les tests lancés, vous pouvez ajuster les paramètres et tester différentes questions pour évaluer les performances du modèle.

```python
output = model.generate(input_ids, max_length=2048, num_beams=64, do_sample=False, early_stopping=True)
```
- `max_length=2048` : Définit la longueur maximale de la séquence générée (2048 tokens ici).
- `num_beams=64` : Utilise la recherche en faisceaux avec 64 faisceaux pour une meilleure qualité de génération.
- `do_sample=False` : Désactive l'échantillonnage, la génération est basée sur la probabilité maximale à chaque étape.
- `early_stopping=True` : Arrête la génération dès que tous les faisceaux ont atteint la fin du texte ou un critère d'arrêt.

---

### 3. Prérequis matériels

- **CPU puissant** : Si vous exécutez le modèle sur votre propre machine, assurez-vous d'avoir un processeur performant.
- **GPU recommandé** : L'exécution sur un **GPU** accélérera considérablement le processus d'inférence, surtout pour des modèles de taille moyenne comme `t5-small`.
  
Nous vous recommandons fortement d'utiliser **Google Colab** si vous n'avez pas accès à un GPU, car il offre un accès gratuit à des ressources GPU puissantes, ce qui est idéal pour ce type de projet.


## License

Ce projet est sous [la licence MIT](LICENSE).
