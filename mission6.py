# =====================================================
#  Mission 6 - Animation : faire defiler le motif
# =====================================================
# A chaque etape, TOUTES les lignes sont decalees d'une colonne vers la
# gauche ; la LED qui sort a gauche revient a droite (rebouclage).
# Affichez l'etat initial, puis les ETAPES etats suivants,
# separes par une ligne vide.

TAILLE = 8
ETAPES = 3

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

# --- affichage de l'etat initial (donne) ---
for i in range(TAILLE):
    texte = ""
    for j in range(TAILLE):
        if matrice[i][j] == 1:
            texte = texte + "# "
        else:
            texte = texte + ". "
    print(texte)

# --- decalages ---
for etape in range(ETAPES):
    # TODO : decaler chaque ligne d'une colonne vers la gauche.
    #        Indice : memoriser matrice[i][0] AVANT de decaler,
    #        puis le replacer en derniere colonne.

    print()
    # TODO : afficher la matrice apres decalage
