#!/usr/bin/env python
# -*- coding: utf-8 -*-
class ContextManagedList:
    def __init__(self, l:list) -> None:
        print("ctor")
        self.l = l

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

# TODO: Importez vos modules ici

# TODO: Définissez vos fonction ici

# EXERCICE 1: Écrire un programme qui compare le contenu de deux fichiers et signale la première différence rencontrée.
def compare_files(nom_fichier_1: str, nom_fichier_2: str):
    with open(nom_fichier_1, "r") as f1, open(nom_fichier_2, "r") as f2:
        same = True
        while same:
            a = f1.read()
            b = f2.read()
            same = a == b
    return -1 if same else f1.tell()

#EXERCICE 2: Écrire un programme qui recopie un fichier texte en triplant tous les espaces entre les mots.
#(vous pouvez ouvrir deux fichiers avec l’instruction with)

def triple_space(file1, file2):
    with open(file1, "r") as data, open(file1, "w") as result:
        text = data.read()
        new_text = text.replace(" ", "   ")
        result.write(new_text)
#EXERCICE 3: Écrire un programme qui lit chaque ligne d’un fichier notes.txt (chaque ligne contient une note en pourcentage) et qui réécrit, dans un nouveau fichier, les notes avec, à coté, les mentions « A », « B », etc. en fonction d’un tableau de correspondance fourni.

#EXERCICE 4: Reprenez l’exercice du livre de recettes et créer une base de données dans un fichier qui permet d’ajouter, modifier, supprimer des recettes. Vous êtes libre de choisir le type de format de fichier.

#EXERCICE 5: Écrire un programme qui lit un fichier texte exemple.txt et retourne une liste de tous les nombres présents dans le fichier, en ordre croissant. 
def find_numbers(file) -> list:
    with open(file) as f:
        text = f.read()
        list_numbers = []
        
    return list_numbers
#EXERCICE 6: Écrire un programme qui lit un fichier et qui recopie une ligne sur deux dans un autre fichier.
def copy_lines(file1,file2):


    pass


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    #with ContextManagedList([1,2]) as my_list:
     #   raise(Exception)

    with open() as a, open() as b:
        pass