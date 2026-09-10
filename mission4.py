# =====================================================
#  Mission 4 - Dessiner des figures dans la matrice
# =====================================================
# Trois figures, chacune affichee a la suite (separees par une ligne vide) :
#   Figure 1 : le cadre  -> toutes les LED du pourtour
#   Figure 2 : la croix  -> les deux diagonales
#   Figure 3 : le logo   -> le cadre AJOUTE a la croix precedente
#
# Le code de construction et d'affichage vous est donne : il est identique
# a celui de la mission 2. Vous n'avez a ecrire que les figures.

TAILLE = 8

# ---------- Figure 1 : le cadre ----------
matrice = []
for i in range(TAILLE):
    ligne = []
    for j in range(TAILLE):
        ligne.append(0)
    matrice.append(ligne)

# TODO : allumer les LED du pourtour
#        (premiere ligne, derniere ligne, premiere colonne, derniere colonne)


for i in range(TAILLE):
    texte = ""
    for j in range(TAILLE):
        if matrice[i][j] == 1:
            texte = texte + "# "
        else:
            texte = texte + ". "
    print(texte)

# ---------- Figure 2 : la croix diagonale ----------
matrice = []
for i in range(TAILLE):
    ligne = []
    for j in range(TAILLE):
        ligne.append(0)
    matrice.append(ligne)

# TODO : allumer les deux diagonales.
#        Une seule boucle suffit : pour la ligne i, quelles colonnes ?


print()
for i in range(TAILLE):
    texte = ""
    for j in range(TAILLE):
        if matrice[i][j] == 1:
            texte = texte + "# "
        else:
            texte = texte + ". "
    print(texte)

# ---------- Figure 3 : le logo (cadre + croix) ----------
# TODO : sans effacer la croix, rallumer le cadre par-dessus


print()
for i in range(TAILLE):
    texte = ""
    for j in range(TAILLE):
        if matrice[i][j] == 1:
            texte = texte + "# "
        else:
            texte = texte + ". "
    print(texte)
