# Test technique – Détection de fraude sur carte d'identité française

## 📋 Introduction

Vous êtes développeur au sein d'une équipe spécialisée dans la lutte contre la fraude documentaire.
Votre mission consiste à analyser des cartes nationales d'identité françaises **dernier format** afin de détecter incohérences, anomalies et tentatives de falsification.

### 📦 Ressources fournies

- 📄 Un **document PDF** d'une carte d'identité française (recto/verso)
- 📝 Un **fichier JSON** contenant le texte extrait sur chaque page par notre outil d'OCR

> **🎯 Objectif**  
> Créer un script **Python** par exercice. Le code doit être **générique et réutilisable** : privilégiez une approche dynamique qui pourra s'appliquer à n'importe quelle CNI du même format, en évitant au maximum le hardcodage de valeurs spécifiques à cet exemple.
>
> **💻 Bonnes pratiques**  
> L'usage de classes ou dataclasses est encouragé pour structurer vos données et votre code.

---

## 🔍 Exercice 1 – Extraction du QR code et vérification de concordance

**Objectif :** exploiter les données encodées dans le QR code présent sur le document et vérifier leur cohérence avec le contenu visible sur la carte.

### Travail attendu

- Extraire et décoder la chaîne contenue dans le QR code
- Nettoyer et parser les informations obtenues
- Comparer ces données avec le contenu visible de la carte d'identité issu de l'OCR (hors MRZ)
- Produire un rapport indiquant clairement où les informations concordent ou divergent

> **💡 Note**  
> L'approche, la structure du code et les choix techniques vous appartiennent.

---

## 📊 Exercice 2 – Parsing des bandes MRZ et cohérence avec le corps de la carte

**Objectif :** analyser les bandes MRZ extraites par l'OCR et vérifier leur cohérence avec les champs "lisibles" de la carte.

### Travail attendu

- Extraire et parser les lignes MRZ présentes dans le JSON
- Vérifier les informations issues de la MRZ (dates, numéro de document, identité, etc.) en les comparant au reste des données du texte extrait par l'OCR
- Identifier et signaler toute incohérence ou information suspecte

> **💡 Note**  
> Là encore, le format de sortie final est laissé à votre appréciation.

---

## 🛡️ Exercice 3 – Contrôles de fraude supplémentaires sur le document

**Objectif :** libre.

### Travail attendu

- Implémenter tous contrôles complémentaires que vous estimez pertinents pour détecter une fraude potentielle sur la carte

---

## 📦 Rendu final attendu

Le rendu devra prendre la forme d'un **dossier zippé** incluant :

| Fichier            | Description                                       |
| ------------------ | ------------------------------------------------- |
| `exercise_1.py`    | Script pour l'exercice 1                          |
| `exercise_2.py`    | Script pour l'exercice 2                          |
| `exercise_3.py`    | Script pour l'exercice 3                          |
| `remarks.md`       | Vos remarques et observations sur chaque exercice |
| `requirements.txt` | Dépendances Python (si nécessaire)                |
| Autres fichiers    | Configuration, helpers, etc. (si nécessaire)      |
