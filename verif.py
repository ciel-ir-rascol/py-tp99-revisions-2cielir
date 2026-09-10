ATTENDUS = {'mission1.py': [('Coordonnees hors matrice',
                  '3\n9\n',
                  'Ligne : Colonne : Erreur : coordonnees hors de la matrice\n'),
                 ('LED du bord', '0\n5\n', 'Ligne : Colonne : LED de bordure\n'),
                 ('LED du bord (coin)', '7\n7\n', 'Ligne : Colonne : LED de bordure\n'),
                 ('LED de la diagonale', '3\n3\n', 'Ligne : Colonne : LED de la diagonale\n'),
                 ('LED interne', '2\n5\n', 'Ligne : Colonne : LED interne\n')],
 'mission2.py': [('Matrice eteinte puis deux LED allumees',
                  '',
                  '. . . . . . . . \n'
                  '. . . . . . . . \n'
                  '. . . . . . . . \n'
                  '. . . . . . . . \n'
                  '. . . . . . . . \n'
                  '. . . . . . . . \n'
                  '. . . . . . . . \n'
                  '. . . . . . . . \n'
                  '\n'
                  '. . . . . . . . \n'
                  '. . . . . . . . \n'
                  '. . . # . . . . \n'
                  '. . . . . . . . \n'
                  '. . . . . . . . \n'
                  '. . . . . # . . \n'
                  '. . . . . . . . \n'
                  '. . . . . . . . \n')],
 'mission3.py': [('Chenillard aller-retour',
                  '',
                  '# . . . . . . . \n'
                  '. # . . . . . . \n'
                  '. . # . . . . . \n'
                  '. . . # . . . . \n'
                  '. . . . # . . . \n'
                  '. . . . . # . . \n'
                  '. . . . . . # . \n'
                  '. . . . . . . # \n'
                  '. . . . . . # . \n'
                  '. . . . . # . . \n'
                  '. . . . # . . . \n'
                  '. . . # . . . . \n'
                  '. . # . . . . . \n'
                  '. # . . . . . . \n')],
 'mission4.py': [('Cadre, croix et logo',
                  '',
                  '# # # # # # # # \n'
                  '# . . . . . . # \n'
                  '# . . . . . . # \n'
                  '# . . . . . . # \n'
                  '# . . . . . . # \n'
                  '# . . . . . . # \n'
                  '# . . . . . . # \n'
                  '# # # # # # # # \n'
                  '\n'
                  '# . . . . . . # \n'
                  '. # . . . . # . \n'
                  '. . # . . # . . \n'
                  '. . . # # . . . \n'
                  '. . . # # . . . \n'
                  '. . # . . # . . \n'
                  '. # . . . . # . \n'
                  '# . . . . . . # \n'
                  '\n'
                  '# # # # # # # # \n'
                  '# # . . . . # # \n'
                  '# . # . . # . # \n'
                  '# . . # # . . # \n'
                  '# . . # # . . # \n'
                  '# . # . . # . # \n'
                  '# # . . . . # # \n'
                  '# # # # # # # # \n')],
 'mission5.py': [('Analyse du motif',
                  '',
                  '. . # # # # . . \n'
                  '. # . . . . # . \n'
                  '# . # . . # . # \n'
                  '# . . . . . . # \n'
                  '# . # . . # . # \n'
                  '# . # # # # . # \n'
                  '. # . . . . # . \n'
                  '. . # # # # . . \n'
                  '\n'
                  'LED allumees : 28\n'
                  'Courant total : 560 mA\n'
                  'Ligne la plus allumee : 5 (6 LED)\n'
                  'Colonne la plus allumee : 2 (5 LED)\n')],
 'mission6.py': [('Defilement du motif',
                  '',
                  '. . # # # # . . \n'
                  '. # . . . . # . \n'
                  '# . # . . # . # \n'
                  '# . . . . . . # \n'
                  '# . # . . # . # \n'
                  '# . # # # # . # \n'
                  '. # . . . . # . \n'
                  '. . # # # # . . \n'
                  '\n'
                  '. # # # # . . . \n'
                  '# . . . . # . . \n'
                  '. # . . # . # # \n'
                  '. . . . . . # # \n'
                  '. # . . # . # # \n'
                  '. # # # # . # # \n'
                  '# . . . . # . . \n'
                  '. # # # # . . . \n'
                  '\n'
                  '# # # # . . . . \n'
                  '. . . . # . . # \n'
                  '# . . # . # # . \n'
                  '. . . . . # # . \n'
                  '# . . # . # # . \n'
                  '# # # # . # # . \n'
                  '. . . . # . . # \n'
                  '# # # # . . . . \n'
                  '\n'
                  '# # # . . . . # \n'
                  '. . . # . . # . \n'
                  '. . # . # # . # \n'
                  '. . . . # # . . \n'
                  '. . # . # # . # \n'
                  '# # # . # # . # \n'
                  '. . . # . . # . \n'
                  '# # # . . . . # \n')]}


# =====================================================================
#  Ne modifiez rien ci-dessous : ce script se contente de lancer vos
#  fichiers missionX.py et de comparer ce qu'ils affichent avec ce qui
#  est attendu. Il ne remplace pas la correction de l'enseignant :
#  la qualite de votre code compte aussi !
# =====================================================================

import os
import subprocess
import sys

INVITES = ["Ligne : ", "Colonne : "]


def normaliser(texte):
    """Enleve les invites de saisie, les espaces de fin de ligne
    et les lignes vides finales."""
    for invite in INVITES:
        texte = texte.replace(invite, "")
    lignes = [ligne.rstrip() for ligne in texte.split("\n")]
    while lignes and lignes[-1] == "":
        lignes.pop()
    return lignes


def premiere_difference(obtenu, attendu):
    for k in range(max(len(obtenu), len(attendu))):
        ligne_obtenue = obtenu[k] if k < len(obtenu) else "(rien)"
        ligne_attendue = attendu[k] if k < len(attendu) else "(rien)"
        if ligne_obtenue != ligne_attendue:
            return k + 1, ligne_obtenue, ligne_attendue
    return None


def main():
    dossier = os.path.dirname(os.path.abspath(__file__))
    reussis = 0
    total = 0
    print("=== Verification du TP Matrice LED ===\n")

    for fichier, cas in ATTENDUS.items():
        chemin = os.path.join(dossier, fichier)
        print("--- " + fichier + " ---")
        if not os.path.exists(chemin):
            print("  fichier introuvable, mission ignoree\n")
            continue

        for nom, entree, sortie_attendue in cas:
            total += 1
            try:
                resultat = subprocess.run(
                    [sys.executable, chemin],
                    input=entree,
                    capture_output=True,
                    text=True,
                    timeout=10,
                    cwd=dossier,
                )
            except subprocess.TimeoutExpired:
                print("  [KO] " + nom + " : le programme ne s'arrete pas "
                      "(boucle infinie ? input() en trop ?)")
                continue

            if resultat.returncode != 0:
                derniere = resultat.stderr.strip().split("\n")[-1]
                print("  [KO] " + nom + " : le programme plante -> " + derniere)
                continue

            obtenu = normaliser(resultat.stdout)
            attendu = normaliser(sortie_attendue)
            difference = premiere_difference(obtenu, attendu)
            if difference is None:
                print("  [OK] " + nom)
                reussis += 1
            else:
                numero, ligne_obtenue, ligne_attendue = difference
                if ligne_attendue == "":
                    ligne_attendue = "(ligne vide)"
                if ligne_obtenue == "":
                    ligne_obtenue = "(ligne vide)"
                print("  [KO] " + nom + " : premiere difference ligne " + str(numero))
                print("       attendu : " + ligne_attendue)
                print("       obtenu  : " + ligne_obtenue)
        print()

    print("=== " + str(reussis) + " / " + str(total) + " tests reussis ===")


main()
