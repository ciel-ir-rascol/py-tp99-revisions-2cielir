# =====================================================
#  Mission 5 - Analyser un motif
# =====================================================
# Le motif est fourni. Vous devez le mesurer.
# Affichages attendus, dans cet ordre et avec exactement ce texte :
#   LED allumees : ...
#   Courant total : ... mA
#   Ligne la plus allumee : i (n LED)
#   Colonne la plus allumee : j (n LED)
# En cas d'egalite, on garde la plus petite ligne / colonne.

TAILLE = 8
COURANT_LED = 20   # milliamperes consommes par une LED allumee

# --- motif fourni : ne pas modifier ---
matrice = [
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
]

# --- affichage du motif (donne) ---
for i in range(TAILLE):
    texte = ""
    for j in range(TAILLE):
        if matrice[i][j] == 1:
            texte = texte + "# "
        else:
            texte = texte + ". "
    print(texte)

print()

# --- 1. nombre total de LED allumees ---
# TODO


# --- 2. courant total consomme (en mA) ---
# TODO


# --- 3. ligne la plus allumee ---
# TODO : compter les LED de chaque ligne et retenir la meilleure


# --- 4. colonne la plus allumee ---
# TODO : attention, ici la boucle des colonnes est a l'exterieur
