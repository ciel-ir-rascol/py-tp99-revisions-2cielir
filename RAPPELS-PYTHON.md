# Rappels Python — l'essentiel de la 1ère année

> Mémo à garder ouvert pendant le TP. Tout ce dont vous avez besoin pour la [mission en cours](README.md) est ici.

## Sommaire

1. [Variables, types et affichage](#1-variables-types-et-affichage)
2. [Saisie au clavier](#2-saisie-au-clavier)
3. [Structures alternatives](#3-structures-alternatives)
4. [Structures répétitives](#4-structures-répétitives)
5. [Les listes](#5-les-listes)
6. [Les listes de listes (matrices)](#6-les-listes-de-listes-matrices)
7. [Les pièges classiques](#7-les-pièges-classiques)

---

## 1. Variables, types et affichage

```python
taille = 8            # int   : nombre entier
courant = 19.5        # float : nombre à virgule
message = "LED"       # str   : chaîne de caractères
allumee = True        # bool  : True ou False
```

Une variable n'a pas besoin d'être déclarée : elle existe dès la première affectation.

### print()

```python
print("Bonjour")                  # Bonjour
print("Total :", 28)              # Total : 28      <- la virgule ajoute UN espace
print("Total : " + str(28))       # Total : 28      <- concaténation, il faut str()
print(28, "LED", "->", 560, "mA") # 28 LED -> 560 mA
print()                           # affiche une ligne vide
```

> [!IMPORTANT]
> `"Total : " + 28` provoque une **erreur** : on ne concatène pas un `str` et un `int`.
> Soit on utilise la virgule dans `print`, soit on convertit avec `str(28)`.

### Construire une chaîne petit à petit

Très utile pour afficher une ligne de LED **sans** aller à la ligne à chaque fois :

```python
texte = ""
texte = texte + "# "
texte = texte + ". "
print(texte)          # affiche : # .
```

---

## 2. Saisie au clavier

`input()` renvoie **toujours** une chaîne de caractères. Pour obtenir un nombre, il faut convertir :

```python
nom = input("Votre nom : ")           # str
age = int(input("Votre age : "))      # int
prix = float(input("Prix : "))        # float
```

---

## 3. Structures alternatives

```python
if condition1:
    # instructions si condition1 est vraie
elif condition2:
    # instructions si condition1 est fausse ET condition2 vraie
else:
    # instructions dans tous les autres cas
```

L'**indentation** (4 espaces) délimite les blocs : c'est elle qui dit ce qui est « dans » le `if`.

### Opérateurs de comparaison

| Opérateur | Signification |
| :---: | --- |
| `==` | égal à (**deux** signes `=`) |
| `!=` | différent de |
| `<` `>` | strictement inférieur / supérieur |
| `<=` `>=` | inférieur / supérieur ou égal |

### Opérateurs logiques

| Opérateur | Vrai quand… | Exemple |
| :---: | --- | --- |
| `and` | les **deux** conditions sont vraies | `if i >= 0 and i < 8:` |
| `or` | **au moins une** des deux est vraie | `if i == 0 or i == 7:` |
| `not` | la condition est fausse | `if not allumee:` |

Python accepte aussi l'écriture mathématique : `if 0 <= i < 8:` est équivalent à `if i >= 0 and i < 8:`.

> [!NOTE]
> Dans un `if / elif / elif / else`, **le premier cas vrai gagne** et les suivants ne sont jamais testés.
> L'ordre des tests fait donc partie de l'énoncé : `(0, 0)` est à la fois une LED de bordure et une LED
> de la diagonale — si le test « bordure » est écrit en premier, la réponse est « bordure ».

---

## 4. Structures répétitives

### while — « tant que »

On l'utilise quand on **ne sait pas à l'avance** combien de tours seront faits.

```python
choix = ""
while choix != "0":
    choix = input("Votre choix : ")
```

### for — « pour chaque »

On l'utilise quand le nombre de tours **est connu**.

```python
for i in range(8):          # i vaut 0, 1, 2, 3, 4, 5, 6, 7  (8 exclu !)
    print(i)
```

### range() sous toutes ses formes

| Écriture | Valeurs prises |
| --- | --- |
| `range(8)` | 0 1 2 3 4 5 6 7 |
| `range(2, 6)` | 2 3 4 5 |
| `range(0, 8, 2)` | 0 2 4 6 |
| `range(6, 0, -1)` | 6 5 4 3 2 1 **(compte à l'envers)** |

> [!IMPORTANT]
> La borne de fin est **toujours exclue**. `range(6, 0, -1)` ne descend donc pas jusqu'à 0.

### Boucles imbriquées

La boucle intérieure fait **un tour complet** à chaque tour de la boucle extérieure :

```python
for i in range(3):        # i = ligne
    for j in range(4):    # j = colonne
        print(i, j)
```
affiche `0 0`, `0 1`, `0 2`, `0 3`, puis `1 0`, `1 1`, … soit 3 × 4 = 12 lignes.

C'est **le** schéma de parcours d'une matrice : `i` parcourt les lignes, `j` les colonnes.
Et si on a besoin de travailler colonne par colonne, il suffit d'échanger les deux boucles :
`j` à l'extérieur, `i` à l'intérieur.

---

## 5. Les listes

```python
barre = [0, 0, 1, 0]      # liste de 4 entiers
print(barre[2])           # 1        <- le premier élément a l'indice 0
barre[0] = 1              # on modifie l'élément d'indice 0
print(len(barre))         # 4        <- nombre d'éléments
barre.append(0)           # ajoute un 0 à la fin -> [1, 0, 1, 0, 0]
```

> [!IMPORTANT]
> Une liste de `n` éléments a des indices allant de `0` à `n - 1`.
> Le dernier élément d'une liste de 8 LED est donc `barre[7]`, jamais `barre[8]`.

### Construire une liste de zéros

```python
barre = []
for i in range(8):
    barre.append(0)
```

### Deux façons de parcourir une liste

```python
for valeur in barre:        # par valeur : pratique pour LIRE
    print(valeur)

for i in range(len(barre)): # par indice : obligatoire pour MODIFIER
    barre[i] = 0
```

---

## 6. Les listes de listes (matrices)

Une matrice est une **liste dont chaque élément est une liste** : une liste de lignes.

```python
matrice = [
    [0, 0, 1],
    [1, 0, 0],
]
print(matrice[1][2])    # 0   -> ligne 1, colonne 2
matrice[0][1] = 1       # allume la case ligne 0, colonne 1
print(len(matrice))     # 2   -> nombre de lignes
print(len(matrice[0]))  # 3   -> nombre de colonnes
```

L'ordre est **toujours** `matrice[ligne][colonne]`.

### Construire une matrice 8 × 8 de zéros

```python
matrice = []
for i in range(8):
    ligne = []            # une nouvelle liste à chaque tour
    for j in range(8):
        ligne.append(0)
    matrice.append(ligne)
```

### Parcourir une matrice

```python
for i in range(8):            # pour chaque ligne
    for j in range(8):        # pour chaque colonne de cette ligne
        print(matrice[i][j])
```

### Repères utiles dans une matrice `n × n`

| Ce qu'on cherche | Condition |
| --- | --- |
| première / dernière ligne | `i == 0` / `i == n - 1` |
| première / dernière colonne | `j == 0` / `j == n - 1` |
| le pourtour (cadre) | `i == 0 or i == n - 1 or j == 0 or j == n - 1` |
| diagonale principale (↘) | `j == i` |
| autre diagonale (↙) | `j == n - 1 - i` |

---

## 7. Les pièges classiques

> [!WARNING]
> **`[[0] * 8] * 8` ne crée pas une matrice utilisable.**
> Cette écriture recopie **8 fois la même ligne** : modifier `matrice[0][0]` modifie la
> première case des 8 lignes en même temps. Construisez toujours la matrice avec deux
> boucles, comme montré plus haut.

| Symptôme | Cause probable |
| --- | --- |
| `IndentationError` | indentation incohérente (mélange d'espaces et de tabulations) |
| `SyntaxError` sur un `if` / `for` | les deux points `:` de fin de ligne ont été oubliés |
| `IndexError: list index out of range` | indice trop grand : on va jusqu'à `n` au lieu de `n - 1` |
| `TypeError: can only concatenate str` | concaténation d'un `str` et d'un `int` sans `str()` |
| Toutes les lignes de la matrice changent ensemble | le piège `[[0] * 8] * 8` |
| La boucle ne s'arrête jamais | dans un `while`, la variable testée n'est jamais modifiée |
| Une seule ligne s'affiche | `print` placé dans la mauvaise boucle (mauvaise indentation) |
