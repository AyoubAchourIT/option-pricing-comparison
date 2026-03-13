# Comparaison de Méthodes de Pricing d'une Option Call Européenne

Ce projet Python propose une démonstration simple de trois méthodes classiques pour valoriser une option call européenne :

- la formule fermée de Black-Scholes
- la simulation de Monte Carlo
- l'arbre binomial de Cox-Ross-Rubinstein (CRR)

L'objectif est pédagogique : comparer plusieurs approches de pricing dans un script clair et facile à lire.

## Paramètres utilisés

Les calculs sont réalisés avec les paramètres suivants :

- `S0 = 100` : prix initial du sous-jacent
- `K = 100` : prix d'exercice
- `r = 3%` : taux sans risque
- `sigma = 20%` : volatilité
- `T = 1` : maturité en année

## Méthodes comparées

### 1. Black-Scholes

Cette méthode utilise la formule analytique standard pour le prix d'un call européen.

### 2. Monte Carlo

Cette méthode simule de nombreux prix terminaux du sous-jacent sous l'hypothèse Black-Scholes, puis calcule la moyenne actualisée des payoffs.

### 3. Arbre binomial CRR

Cette méthode discrétise l'évolution du sous-jacent dans un arbre binomial et utilise une induction à rebours pour obtenir le prix de l'option.

## Résultats produits

Le script :

- affiche le prix obtenu avec chaque méthode
- affiche les écarts entre les méthodes
- génère un graphique de convergence du prix binomial vers le prix Black-Scholes
- sauvegarde ce graphique dans le fichier `binomial_convergence.png`

## Exécution du projet

### 1. Installer les dépendances

```bash
pip install -r requirements.txt

pip install -r requirements.txt
### 2. Lancer le script
```bash
python option_pricing_comparison.py
## Fichiers du projet
- option_pricing_comparison.py : script principal
- requirements.txt : dépendances Python
- README.md : présentation du projet

## Public visé
Ce dépôt est adapté à une démonstration de cours ou à une première introduction aux méthodes numériques et analytiques utilisées en finance quantitative.
