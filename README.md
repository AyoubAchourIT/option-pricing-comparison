# Comparaison de Methodes de Pricing d'une Option Call Europeenne

Ce projet Python propose une demonstration simple de trois methodes classiques pour valoriser une option call europeenne :

- la formule fermee de Black-Scholes
- la simulation de Monte Carlo
- l'arbre binomial de Cox-Ross-Rubinstein (CRR)

L'objectif est pedagogique : comparer plusieurs approches de pricing dans un script clair et facile a lire.

## Parametres utilises

Les calculs sont realises avec les parametres suivants :

- `S0 = 100` : prix initial du sous-jacent
- `K = 100` : prix d'exercice
- `r = 3%` : taux sans risque
- `sigma = 20%` : volatilite
- `T = 1` : maturite en annee

## Methodes comparees

### 1. Black-Scholes

Cette methode utilise la formule analytique standard pour le prix d'un call europeen.

### 2. Monte Carlo

Cette methode simule de nombreux prix terminaux du sous-jacent sous l'hypothese Black-Scholes, puis calcule la moyenne actualisee des payoffs.

### 3. Arbre binomial CRR

Cette methode discretise l'evolution du sous-jacent dans un arbre binomial et utilise une induction a rebours pour obtenir le prix de l'option.

## Resultats produits

Le script :

- affiche le prix obtenu avec chaque methode
- affiche les ecarts entre les methodes
- genere un graphique de convergence du prix binomial vers le prix Black-Scholes
- sauvegarde ce graphique dans le fichier `binomial_convergence.png`

## Execution du projet

### 1. Installer les dependances

```bash
pip install -r requirements.txt
```

### 2. Lancer le script

```bash
python option_pricing_comparison.py
```

## Fichiers du projet

- `option_pricing_comparison.py` : script principal
- `requirements.txt` : dependances Python
- `README.md` : presentation du projet

## Public vise

Ce depot est adapte a une demonstration de cours ou a une premiere introduction aux methodes numeriques et analytiques utilisees en finance quantitative.
