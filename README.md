# TP de révisions Python — L'afficheur à matrice LED

**STS 2CIEL-IR — Durée : 4h — Révisions de l'ensemble du programme Python de 1ère année.**

```text
. . # # # # . .
. # . . . . # .
# . # . . # . #
# . . . . . . #
# . # . . # . #
# . # # # # . #
. # . . . . # .
. . # # # # . .
```

> *Le club robotique du lycée a récupéré un afficheur à **matrice de LED 8 × 8**. Avant de le
> piloter pour de vrai depuis un microcontrôleur, on vous demande d'en écrire le **simulateur**
> en Python : allumer des LED, dessiner des figures, mesurer la consommation, animer un motif.*

Ce TP est un **projet unique** découpé en 6 missions qui se suivent. Chaque mission réutilise ce
que la précédente a mis en place et révise une partie du programme : structures alternatives,
structures répétitives, listes, listes 2D et boucles imbriquées.

👉 **Toutes les notions nécessaires sont rappelées dans [RAPPELS-PYTHON.md](RAPPELS-PYTHON.md).**
Gardez ce fichier ouvert dans un second onglet.

---

## 🚀 Avant de commencer

> [!IMPORTANT]
> **Ce dépôt est votre rendu.**
>
> 1. **Forkez ce dépôt** sur votre compte GitHub — bouton **Fork**, en haut à droite de cette page.
> 2. Clonez **votre fork** sur votre poste, puis ouvrez le dossier dans votre éditeur.
> 3. Complétez les fichiers `mission1.py` à `mission6.py` : chacun contient un squelette et des `TODO`.
> 4. Committez et poussez à la fin de **chaque mission** :
>    ```bash
>    git add .
>    git commit -m "Mission N"
>    git push
>    ```
> 5. Communiquez l'URL de votre fork à l'enseignant en fin de séance.

### Environnement de travail

| | |
| --- | --- |
| **Langage** | Python 3 |
| **Exécution** | `python3 mission1.py` dans un terminal ouvert dans le dossier du dépôt |
| **Fichiers à compléter** | `mission1.py` … `mission6.py`, puis `bonus.py` |
| **Autovérification** | `python3 verif.py` |

### Règles du jeu

> [!WARNING]
> - **Pas de fonctions** dans les missions 1 à 6 : on révise ici le code « au fil de l'eau ».
>   Les fonctions arrivent dans le **bonus**, et vous comprendrez alors pourquoi elles existent.
> - **Pas de modules externes**, pas de `numpy` : listes et boucles uniquement.
> - Ne modifiez pas les lignes déjà écrites dans les squelettes (constantes, motifs fournis,
>   blocs d'affichage donnés) : `verif.py` compte dessus.
> - Nommez vos variables correctement (`ligne`, `colonne`, `total`… et non `a`, `b`, `x1`).

### L'autovérification

Le script `verif.py` lance vos programmes et compare ce qu'ils affichent au résultat attendu :

```bash
python3 verif.py
```

```text
--- mission2.py ---
  [KO] Matrice eteinte puis deux LED allumees : premiere difference ligne 3
       attendu : . . . . . . . .
       obtenu  : . . . . . . .
```

> [!NOTE]
> Les espaces en fin de ligne et les lignes vides à la fin du programme sont ignorés.
> `verif.py` est une **aide**, pas la note : la lisibilité et la justesse de votre code comptent
> tout autant que la sortie affichée.

---

## Convention d'affichage

Une matrice s'affiche **toujours** de la même manière dans tout le TP : une ligne de la matrice
donne une ligne à l'écran, chaque LED est suivie d'un espace.

| Valeur | Affichage |
| :---: | :---: |
| `1` (allumée) | `#` |
| `0` (éteinte) | `.` |

```text
. . # # # # . .     <- ligne 0 : matrice[0]
. # . . . . # .     <- ligne 1
```

Les lignes sont numérotées de haut en bas (`0` à `7`), les colonnes de gauche à droite (`0` à `7`).
La LED en haut à gauche est donc `matrice[0][0]`.

---

## Sommaire

| Mission | Objectif | Notions révisées | Points |
| :---: | --- | --- | :---: |
| **1** | Contrôler la commande d'une LED | alternatives, opérateurs logiques | 3 |
| **2** | Construire et afficher la matrice | listes, listes 2D, boucles imbriquées | 4 |
| **3** | Le chenillard | listes 1D, `range()` à l'envers | 3 |
| **4** | Dessiner des figures | parcours de matrice, conditions sur `i` et `j` | 4 |
| **5** | Analyser un motif | comptage, recherche d'un maximum | 4 |
| **6** | Animer le motif | décalage dans une liste | 2 |
| **Bonus** | Refactoriser en fonctions + menu | fonctions, `while` | — |
| | | **Total** | **/20** |

---

## Mission 1 — Contrôler la commande d'une LED

**Fichier : `mission1.py` — 3 points**

Avant d'allumer quoi que ce soit, le simulateur doit valider la commande reçue. L'opérateur saisit
une ligne et une colonne ; votre programme annonce de quel type de LED il s'agit.

Les règles sont testées **dans cet ordre** :

| Cas | Message à afficher |
| --- | --- |
| Une des deux coordonnées est hors de l'intervalle `0..7` | `Erreur : coordonnees hors de la matrice` |
| La LED est sur le pourtour de la matrice | `LED de bordure` |
| La LED est sur la diagonale principale (`ligne == colonne`) | `LED de la diagonale` |
| Tous les autres cas | `LED interne` |

> [!NOTE]
> L'ordre compte : la LED `(0, 0)` est à la fois sur le bord et sur la diagonale.
> Comme le test « bordure » vient avant, la réponse attendue est `LED de bordure`.

### Exemples d'exécution

```text
Ligne : 3
Colonne : 9
Erreur : coordonnees hors de la matrice
```
```text
Ligne : 0
Colonne : 5
LED de bordure
```
```text
Ligne : 3
Colonne : 3
LED de la diagonale
```
```text
Ligne : 2
Colonne : 5
LED interne
```

> 💡 Les deux lignes `input()` sont déjà écrites dans le squelette : n'y touchez pas.
> Utilisez la constante `TAILLE` plutôt que d'écrire `8` un peu partout.

---

## Mission 2 — Construire et afficher la matrice

**Fichier : `mission2.py` — 4 points**

C'est le cœur du simulateur : la mémoire de l'afficheur.

1. **Construire** une matrice de `TAILLE` × `TAILLE` remplie de `0`, à l'aide de deux boucles
   et de `.append()`.
2. **L'afficher** selon la convention ci-dessus.
3. **Allumer** les LED `(2, 3)` et `(5, 5)`, afficher **une ligne vide**, puis réafficher la matrice.

> [!WARNING]
> L'écriture `matrice = [[0] * 8] * 8` semble marcher… jusqu'à ce que vous allumiez une LED :
> les 8 lignes s'allument ensemble. Voir la section *Les pièges classiques* des rappels.

### Sortie attendue

```text
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .

. . . . . . . .
. . . . . . . .
. . . # . . . .
. . . . . . . .
. . . . . . . .
. . . . . # . .
. . . . . . . .
. . . . . . . .
```

> 💡 Pour afficher une ligne complète **sans** revenir à la ligne à chaque LED, construisez
> d'abord la chaîne `texte` LED par LED, puis faites un seul `print(texte)` à la fin de la ligne.

---

## Mission 3 — Le chenillard

**Fichier : `mission3.py` — 3 points**

On met la matrice de côté : ici, l'afficheur n'utilise qu'**une seule liste de 8 LED**.
Une seule LED est allumée à la fois et se déplace, comme les feux d'une voiture de police.

- **Aller** : la LED allumée va de la position `0` à la position `7` → 8 lignes affichées.
- **Retour** : elle repart de la position `6` jusqu'à la position `1` → 6 lignes affichées.

À chaque étape, on éteint tout, on allume la bonne LED, puis on affiche la barre sur une ligne.

### Sortie attendue

```text
# . . . . . . .
. # . . . . . .
. . # . . . . .
. . . # . . . .
. . . . # . . .
. . . . . # . .
. . . . . . # .
. . . . . . . #
. . . . . . # .
. . . . . # . .
. . . . # . . .
. . . # . . . .
. . # . . . . .
. # . . . . . .
```

> 💡 Le retour ne réaffiche ni la position `7` ni la position `0` : sinon l'animation
> marquerait un temps d'arrêt aux extrémités. Un `range()` qui compte à l'envers fait ça très bien.

---

## Mission 4 — Dessiner des figures

**Fichier : `mission4.py` — 4 points**

Retour à la matrice 2D. Trois figures, affichées à la suite et séparées par une ligne vide.
Le code de construction et d'affichage vous est **donné** dans le squelette : concentrez-vous sur
les conditions qui déterminent quelles LED allumer.

1. **Le cadre** : toutes les LED du pourtour, sur une matrice neuve.
2. **La croix** : les deux diagonales, sur une matrice neuve. Une seule boucle suffit.
3. **Le logo** : le cadre rallumé **par-dessus** la croix précédente (sans l'effacer).

### Sortie attendue

```text
# # # # # # # #
# . . . . . . #
# . . . . . . #
# . . . . . . #
# . . . . . . #
# . . . . . . #
# . . . . . . #
# # # # # # # #

# . . . . . . #
. # . . . . # .
. . # . . # . .
. . . # # . . .
. . . # # . . .
. . # . . # . .
. # . . . . # .
# . . . . . . #

# # # # # # # #
# # . . . . # #
# . # . . # . #
# . . # # . . #
# . . # # . . #
# . # . . # . #
# # . . . . # #
# # # # # # # #
```

> 💡 Le tableau *Repères utiles dans une matrice* des rappels donne les conditions
> à écrire pour le pourtour et pour chacune des deux diagonales.

---

## Mission 5 — Analyser un motif

**Fichier : `mission5.py` — 4 points**

Le motif (un visage) est **fourni** dans le squelette, ainsi que son affichage. Vous devez le
mesurer, notamment pour vérifier que l'alimentation de la maquette tiendra le coup : chaque LED
allumée consomme `COURANT_LED` = 20 mA.

Affichez, dans cet ordre et avec exactement ce texte :

1. `LED allumees : <nombre total de LED allumées>`
2. `Courant total : <nombre> mA`
3. `Ligne la plus allumee : <numéro> (<nombre> LED)`
4. `Colonne la plus allumee : <numéro> (<nombre> LED)`

En cas d'égalité, on retient la ligne (ou la colonne) de plus petit numéro.

### Sortie attendue

```text
. . # # # # . .
. # . . . . # .
# . # . . # . #
# . . . . . . #
# . # . . # . #
# . # # # # . #
. # . . . . # .
. . # # # # . .

LED allumees : 28
Courant total : 560 mA
Ligne la plus allumee : 5 (6 LED)
Colonne la plus allumee : 2 (5 LED)
```

> 💡 Pour la question 4, la boucle des **colonnes** doit être à l'extérieur et celle des lignes à
> l'intérieur : on parcourt la matrice « verticalement ». Pour chercher un maximum, on garde deux
> variables (le meilleur compte trouvé et l'indice correspondant) que l'on met à jour ensemble.

---

## Mission 6 — Animer le motif

**Fichier : `mission6.py` — 2 points**

Dernière étape avant l'affichage réel : faire **défiler** le motif vers la gauche, comme un
bandeau publicitaire. À chaque étape, toutes les lignes sont décalées d'une colonne vers la
gauche, et la LED qui sort à gauche **revient à droite**.

Affichez l'état initial (déjà donné dans le squelette), puis les `ETAPES` états suivants,
séparés par une ligne vide.

### Sortie attendue

```text
. . # # # # . .
. # . . . . # .
# . # . . # . #
# . . . . . . #
# . # . . # . #
# . # # # # . #
. # . . . . # .
. . # # # # . .

. # # # # . . .
# . . . . # . .
. # . . # . # #
. . . . . . # #
. # . . # . # #
. # # # # . # #
# . . . . # . .
. # # # # . . .

# # # # . . . .
. . . . # . . #
# . . # . # # .
. . . . . # # .
# . . # . # # .
# # # # . # # .
. . . . # . . #
# # # # . . . .

# # # . . . . #
. . . # . . # .
. . # . # # . #
. . . . # # . .
. . # . # # . #
# # # . # # . #
. . . # . . # .
# # # . . . . #
```

> 💡 Décalez **une ligne à la fois**. Avant de décaler la ligne `i`, mettez de côté
> `matrice[i][0]` dans une variable : sans ça, la valeur est écrasée et perdue.
> Décalez ensuite chaque case vers la gauche, puis replacez la valeur mise de côté
> dans la dernière colonne.

---

## Bonus — Le vrai simulateur

**Fichier : `bonus.py` — non noté, mais fortement conseillé**

Vous venez de recopier le **même bloc d'affichage** dans cinq fichiers différents. C'est
exactement le problème que résolvent les **fonctions**.

Le squelette contient les fonctions à compléter (`creer_matrice`, `afficher`, `allumer`,
`compter`, `tracer_cadre`, `decaler_gauche`) et un menu déjà écrit. À vous d'écrire le corps
des fonctions, puis de traiter chaque choix du menu en les appelant.

```text
--- Matrice LED 8x8 ---
1. Afficher
2. Allumer une LED
3. Tracer le cadre
4. Decaler vers la gauche
5. Consommation
6. Tout eteindre
0. Quitter
Votre choix :
```

Une fois ce fichier terminé, comparez sa taille à celle de vos six missions mises bout à bout.

---

## Évaluation

| Critère | |
| --- | :---: |
| Missions 1 à 6 fonctionnelles (sortie conforme) | 15 |
| Qualité du code : noms de variables, indentation, absence de code inutile | 3 |
| Utilisation des constantes et commits réguliers sur le fork | 2 |
| | **/20** |
