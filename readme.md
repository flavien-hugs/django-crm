## Django-CRM (Customer Relationship Management ou Gestion de la Relation Client )

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3-orange.svg)](https://djangoproject.com)

Qu'est-ce qu'un CRM ?
Le CRM est l'ensemble des dispositifs ou opérations de marketing ou de support ayant pour but d'optimiser la qualité de la relation client, de fidéliser et de maximiser le chiffre d'affaires ou la marge par client.

### Démarrer le projet en local

Tout d'abord, clonez le dépôt sur votre machine locale:

```bash
git clone https://github.com/flavien-hugs/django-crm
```

Créer un virtualenv

```bash
virtualenv venv
```

Installer les dépendances:

```bash
pip install -r requirements.txt
```

Appliquer les migrations:

```bash
python manage.py migrate
```

Enfin, lancez le serveur:

```bash
python manage.py runserver ou ./manage.py runserver
```

Visitez le projet en local via l'adresse suivante: **127.0.0.1:8000**.
