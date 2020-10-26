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
def exercice1():
    pass
def compare_files(nom_fichier_1: str, nom_fichier_2: str):
    with open(nom_fichier_1, "r") as f1, open(nom_fichier_2, "r") as f2:
        same = True
        while same:
            a = f1.read()
            b = f2.read()
            same = a == b
    return -1 if same else f1.tell()

def exercice2():
    pass
    #Écrire un programme qui recopie un fichier
    # texte en triplant tous les espaces entre les mots.
    #(vous pouvez ouvrir deux fichiers avec l’instruction with)

def triple_space(file1, file2):
    with open(file1, "r") as data, open(file1, "w") as result:
        text = data.read()
        new_text = text.replace(" ", "   ")
        result.write(new_text)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    with ContextManagedList([1,2]) as my_list:
        raise(Exception)

    with open() as a, open() as b:
        pass