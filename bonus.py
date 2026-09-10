# =====================================================
#  Bonus - La meme chose, mais avec des fonctions
# =====================================================
# Vous avez recopie le meme bloc d'affichage dans presque tous les
# fichiers de ce TP : c'est exactement le probleme que resolvent les
# fonctions. Completez celles-ci, puis le menu du programme principal.

TAILLE = 8
COURANT_LED = 20


def creer_matrice():
    """Renvoie une matrice TAILLE x TAILLE entierement eteinte."""
    # TODO


def afficher(matrice):
    """Affiche la matrice : # pour une LED allumee, . pour une LED eteinte."""
    # TODO


def allumer(matrice, ligne, colonne):
    """Allume la LED (ligne, colonne), ou affiche une erreur si elle
    est hors de la matrice."""
    # TODO


def compter(matrice):
    """Renvoie le nombre de LED allumees."""
    # TODO


def tracer_cadre(matrice):
    """Allume les LED du pourtour de la matrice."""
    # TODO


def decaler_gauche(matrice):
    """Decale toutes les lignes d'une colonne vers la gauche, avec rebouclage."""
    # TODO


# ---------------- programme principal ----------------
matrice = creer_matrice()
choix = ""

while choix != "0":
    print()
    print("--- Matrice LED 8x8 ---")
    print("1. Afficher")
    print("2. Allumer une LED")
    print("3. Tracer le cadre")
    print("4. Decaler vers la gauche")
    print("5. Consommation")
    print("6. Tout eteindre")
    print("0. Quitter")
    choix = input("Votre choix : ")

    # TODO : traiter chaque choix en appelant les fonctions ci-dessus
