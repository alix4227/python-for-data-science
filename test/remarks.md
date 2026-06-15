# Test technique – Détection de fraude sur carte d'identité française

---

## 🔍 Exercice 1 – Extraction du QR code et vérification de concordance

**Objectif :** exploiter les données encodées dans le QR code présent sur le document et vérifier leur cohérence avec le contenu visible sur la carte.

### Observations

De nombreuses incohérences ont été relevées entre les données OCRisées et visibles sur la CNI et les données contenues dans le QR code :

- un seul prénom dans le QR code, alors que les données OCRisées indiquent deux prénoms différents ;
- les lieux de naissance sont différents ;
- la CNI indique une nationalité apparemment danoise, alors que le QR code indique une nationalité française (FRA).

Par conséquent, une fraude semble manifeste.

Les résultats des comparaisons sont stockés dans un fichier `report.txt`.

---

## 📊 Exercice 2 – Parsing des bandes MRZ et cohérence avec le corps de la carte

**Objectif :** analyser les bandes MRZ extraites par l'OCR et vérifier leur cohérence avec les champs lisibles de la carte.

### Observations

De nombreuses incohérences ont été relevées entre les données MRZ et les données OCRisées et visibles sur la CNI :

- les numéros de document ne concordent pas ;
- les dates d'expiration ne concordent pas ;
- la CNI indique une nationalité apparemment danoise, alors que les bandes MRZ indiquent une nationalité française (FRA).

Par conséquent, une fraude semble manifeste.

Le parsing est rendu difficile par la structure des bandes MRZ. Certaines informations sont séparées par des chiffres qui semblent calculés par un algorithme. Les dates sont également indiquées en ordre inversé.

---

## 🛡️ Exercice 3 – Contrôles de fraude supplémentaires sur le document

**Objectif :** implémenter tous les contrôles complémentaires jugés pertinents pour détecter une fraude potentielle sur la carte.

### Contrôles proposés

Il semble opportun de vérifier la cohérence des dates :

- La date de délivrance de la CNI est-elle antérieure à la date d'expiration ?
- La date de délivrance ou d'expiration de la CNI est-elle postérieure à la date de naissance ?
- Le délai entre la date de délivrance et la date d'expiration est-il bien de 10 ans ?

On pourrait également comparer l'ensemble des données avec des informations disponibles via des API externes.