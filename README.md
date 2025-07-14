# 🎮 Projet 2048 — Coding Weeks CentraleSupélec

Bienvenue dans notre version personnalisée du jeu **2048**, développée en Python avec **Pygame**, dans le cadre des Coding Weeks à CentraleSupélec.

---

## 📌 Description

Ce projet a été réalisé lors de la **semaine 1** des Coding Weeks, dédiée à la programmation du jeu 2048.  
L'objectif était de :
- comprendre la logique du jeu
- mettre en place une interface interactive avec Pygame
- proposer une version modifiable avec différents paramètres

---

## 🚀 Fonctionnalités principales

- 🧱 **Grille personnalisable** : choisissez la taille (3×3, 4×4, 5×5, etc.)
- 🎨 **Thèmes visuels au choix** :
  - Classique (nombres)
  - Chimie (éléments chimiques)
  - Alphabet (A, B, C…)
- ✅ Contrôles via les flèches du clavier
- 🧪 De nombreux tests unitaires pour valider la logique du jeu

## 📁 Structure du projet

```
.
├── README.md                      # Présentation du projet
├── TemplateProject_2048.md       # Etapes du projet 
├── game2048/                     # Dossier principal contenant le jeu
│   └── display_grid.py           # Script principal pour lancer le jeu
│   └── ...                       # Modules liés à la logique du jeu
├── test_fonctionalite2.py        # Test - Fonctionnalité 2
├── test_fonctionalite4.py        # Test - Fonctionnalité 4
├── test_grid_2048.py             # Test de la logique de grille
├── test_textual_2048.py          # Test des éléments textuels
├── Images/                       # Ressources ou visuels pour le jeu
└── tempCodeRunnerFile.python     # Fichier temporaire généré par l'éditeur
```

🧪 Tous les fichiers de test sont à la racine et couvrent différentes fonctionnalités du jeu.

📄 Le fichier `TemplateProject_2048.md` sert de **guide pédagogique** fourni par les encadrants pour structurer le développement.

🎮 Le dossier `game2048` contient tout le **code source du jeu interactif**.

---

## 🧑‍💻 Lancer le jeu

### 1. Prérequis

Assurez-vous d’avoir installé :
- Python 3.7+
- Pygame (`pip install pygame`)

### 2. Commande de lancement

Dans un terminal, placez-vous dans le dossier `game2048`, puis exécutez :

```bash
python display_grid.py
