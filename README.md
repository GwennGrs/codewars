![Coverage](./coverage.svg)

## Python/Codewars project
Ce projet fais partie des projets à réalisé dans le cadre du cours de Refresher Computer Science

### Contenue:
* Ce code répertorie 10 fichiers Python répondant à des problèmes de difficultés variables.
* Les problèmes sont tirées de Codewars

### Features:
* Chaque code est commenté et détaillé, incluant le lien du problème associé.
* Grace à pytest, chaque code est testé correctement et le badge de coverage associé est présenté dans l'en-tete du ReadME grâce à un workflow github.
* Poetry permet une gestion des dépendances efficaces et une installation du projet rapide.
* Un score **Pylint** de 10 et un message d'erreur dans les actions si le score Pylint est inférieur à 7.5.

### Installation du projet en local:
Installation: 
```git clone git@github.com:GwennGrs/codewars.git```

Pour les dépendances: 
```poetry install```

Pour les tests:
```poetry run pytest```

Pour le score de Pylint:
```poetry run pylint src/codewars```
