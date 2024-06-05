# Pour importer un de ces automates (ou tous) utilisez :
# import Automates
# (pour importer toutes les variables (pour les utiliser après, il faut utiliser Automates.{nom de la variable}))

# from Automates import {nom de la variable}    
# (pour importer uniquement une variable ou plusieurs si vous mettez plusieurs noms de variable)

# from Automates import *
# (pour importer toutes les variables directement (je le déconseille car vous pouvez écraser des variables déjà défini dans votre programme))



# Automates exemples du sujet

auto = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4],
    "transitions":[[1, 'a', 2], [2, 'a', 2], [2, 'b', 3], [3, 'a', 4]],
    "I":[1],
    "F":[4]
}

auto0 = {
    "alphabet": ['a', 'b'],
    "etats": [0, 1, 2, 3],
    "transitions":[[0, 'a', 1],[1, 'a', 1],[1, 'b', 2],[2, 'a', 3]], 
    "I":[0],
    "F":[3]
}

auto1 = {
    "alphabet":['a', 'b'],
    "etats": [0, 1],
    "transitions":[[0, 'a', 0],[0, 'b', 1],[1, 'b', 1],[1, 'a', 1]], 
    "I":[0],
    "F":[1]
}

auto2 = {
    "alphabet":['a', 'b'],
    "etats": [0, 1],
    "transitions":[[0, 'a', 0],[0, 'a', 1],[1, 'b', 1],[1, 'a', 1]], 
    "I":[0],
    "F":[1]
}

auto3 = {
    "alphabet":['a', 'b'],
    "etats": [0, 1, 2],
    "transitions":[[0, 'a', 1],[0, 'a', 0],[1, 'b', 2],[1, 'b', 1]], 
    "I":[0],
    "F":[2]
}

auto4 = {
    "alphabet":['a', 'b'],
    "etats": [0, 1, 2],
    "transitions":[[0, 'a', 1],[1, 'b', 2],[2, 'b', 2],[2, 'a', 2]], 
    "I":[0],
    "F":[2]
}

auto5 = {
    "alphabet":['a', 'b'],
    "etats": [0, 1, 2],
    "transitions":[[0, 'a', 0],[0, 'b', 1],[1, 'a', 1],[1, 'b', 2],[2, 'a', 2],[2, 'b', 0]],
    "I":[0],
    "F":[0, 1]
}

auto6 ={
    "alphabet":['a', 'b'],
    "etats": [0, 1, 2, 3, 4, 5],
    "transitions":[[0, 'a', 4], [0, 'b', 3],[1, 'a', 5],[1, 'b', 5],[2, 'a', 5],[2, 'b', 2],[3, 'a', 1],[3, 'b', 0], [4, 'a', 1],[4, 'b', 2],[5, 'a', 2],[5, 'b', 5]],
    "I":[0],
    "F":[0, 1, 2, 5]
}

# ---------------------------------------------------------------------------------------

# Automate TD 2 ex 1
auto7 = {
    "alphabet": ['a', 'b', 'c'],
    "etats": [1, 2, 3],
    "transitions": [[1, 'a', 2], [2, 'a', 2], [2, 'b', 2], [2, 'c', 2], [2, 'a', 3], [2, 'c', 3]],
    "I": [1],
    "F": [3]
}

# Automates TD 2 ex 2
auto8 = {
    "alphabet": ['a', 'b'],
    "etats": [0, 1, 2],
    "transitions": [[0, 'a', 0], [0, 'b', 1], [1, 'a', 1], [1, 'b', 2], [2, 'a', 2], [2, 'b', 0]],
    "I": [0],
    "F": [0]
}

# Automates TD 2 ex 3 (dans l'ordre)
auto9 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3],
    "transitions": [[1, 'a', 2], [1, 'a', 3], [1, 'b', 2], [1, 'b', 3], [2, 'a', 2], [2, 'a', 3], [2, 'b', 2], [2, 'b', 3]],
    "I": [1],
    "F": [1, 3]
}

auto10 = {
    "alphabet": ['a', 'b'],
    "etats": [1],
    "transitions": [[1, 'a', 1], [1, 'b', 1]],
    "I": [1],
    "F": [1]
}

auto11 = {
    "alphabet": ['a', 'b'],
    "etats": [1],
    "transitions": [],
    "I": [1],
    "F": [1]
}

auto12 = {
    "alphabet": ['a', 'b'],
    "etats": [1],
    "transitions": [[1, 'a', 1], [1, 'b', 1]],
    "I": [1],
    "F": []
}

auto13 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2],
    "transitions": [[1, 'a', 2], [1, 'b', 2], [2, 'a', 2], [2, 'b', 2]],
    "I": [1],
    "F": [2]
}

auto14 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2],
    "transitions": [[1, 'a', 1], [1, 'b', 1], [1, 'b', 2]],
    "I": [1],
    "F": [2]
}

auto15 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2],
    "transitions": [[1, 'a', 1], [1, 'b', 2], [2, 'a', 1], [2, 'b', 2]],
    "I": [1],
    "F": [2]
}

auto16 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2],
    "transitions": [[1, 'a', 1], [1, 'b', 2], [2, 'a', 2], [2, 'b', 1]],
    "I": [1],
    "F": [1]
}

auto17 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4, 5],
    "transitions": [[1, 'b', 2], [1, 'b', 4], [2, 'a', 3], [2, 'b', 3], [3, 'a', 2], [3, 'b', 2], [3, 'b', 4], [5, 'a', 5], [5, 'b', 5], [5, 'a', 4]],
    "I": [1, 5],
    "F": [4]
}

# Automates TD 3 ex 1 (de gauche à droite)
auto18 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3],
    "transitions": [[1, 'b', 2], [1, 'b', 3], [2, 'a', 2], [2, 'a', 3], [2, 'b', 2], [3, 'a', 1], [3, 'a', 3]],
    "I": [1, 2],
    "F": [3]
}

auto19 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4],
    "transitions": [[1, 'a', 2], [1, 'a', 3], [1, 'b', 2], [2, 'a', 4], [2, 'b', 1], [3, 'b', 4], [4, 'a', 2], [4, 'b', 3]],
    "I": [1, 4],
    "F": [3, 4]
}

auto20 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4, 5],
    "transitions": [[1, 'a', 2], [2, 'a', 3], [2, 'b', 1], [2, 'b', 2], [3, 'a', 1], [3, 'b', 1], [3, 'b', 3]],
    "I": [1],
    "F": [1]
}

# Automates TD 3 ex 2
auto21 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4, 5],
    "transitions": [[1, 'a', 2], [2, 'b', 3], [3, 'a', 1], [3, 'b', 4], [5, 'a', 2], [5, 'b', 3]],
    "I": [1],
    "F": [1]
}

# Automates TD 3 ex 3 (dans l'ordre)
auto22 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4],
    "transitions": [[1, 'a', 2], [1, 'b', 1], [2, 'a', 2], [2, 'b', 3], [3, 'a', 4], [3, 'b', 1], [4, 'a', 2], [4, 'b', 3]],
    "I": [1],
    "F": [4]
}

auto23 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4],
    "transitions": [[1, 'a', 2], [1, 'b', 1], [2, 'a', 2], [2, 'b', 3], [3, 'a', 4], [3, 'b', 1], [4, 'a', 2], [4, 'b', 3]],
    "I": [1],
    "F": [1, 2, 3]
}

auto24 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4, 5],
    "transitions": [[1, 'a', 2], [1, 'b', 5], [2, 'a', 5], [2, 'b', 3], [3, 'a', 4], [3, 'b', 5], [4, 'a', 4], [4, 'b', 4], [5, 'a', 5], [5, 'b', 5]],
    "I": [1],
    "F": [4]
}

auto25 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4, 5],
    "transitions": [[1, 'a', 2], [1, 'b', 5], [2, 'a', 5], [2, 'b', 3], [3, 'a', 4], [3, 'b', 5], [4, 'a', 4], [4, 'b', 4], [5, 'a', 5], [5, 'b', 5]],
    "I": [1],
    "F": [1, 2, 3, 5]
}

auto26 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4],
    "transitions": [[1, 'a', 2], [1, 'b', 1], [2, 'a', 2], [2, 'b', 3], [3, 'a', 4], [3, 'b', 1], [4, 'a', 4], [4, 'b', 4]],
    "I": [1],
    "F": [4]
}

# Automates TD 4 ex 1
auto27 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4],
    "transitions": [[1, 'a', 4], [1, 'b', 2], [2, 'a', 3], [2, 'b', 4], [3, 'a', 3], [3, 'b', 3], [4, 'a', 4], [4, 'b', 4]],
    "I": [1],
    "F": [4]
}

auto28 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4],
    "transitions": [[1, 'a', 2], [1, 'b', 1], [2, 'a', 2], [2, 'b', 3], [3, 'a', 4], [3, 'b', 1], [4, 'a', 1], [4, 'b', 3]],
    "I": [1],
    "F": [4]
}

auto29 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4, 5, 6, 7],
    "transitions": [[1, 'a', 7], [1, 'b', 2], [2, 'a', 3], [2, 'b', 4], [3, 'a', 3], [3, 'b', 4], [4, 'a', 5], [4, 'b', 6], [5, 'a', 6], [5, 'b', 4], [6, 'a', 3], [6, 'b', 6], [7, 'a', 7], [7, 'b', 7]],
    "I": [1],
    "F": [4]
}

auto30 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4, 5, 6, 7],
    "transitions": [[1, 'a', 3], [1, 'b', 2], [2, 'a', 4], [2, 'b', 1], [3, 'a', 5], [3, 'b', 4], [4, 'a', 6], [4, 'b', 3], [5, 'a', 7], [5, 'b', 6], [6, 'a', 7], [6, 'b', 5], [7, 'a', 7], [7, 'b', 7]],
    "I": [1],
    "F": [2, 4, 6]
}

auto31 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4, 5, 6],
    "transitions": [[1, 'a', 2], [1, 'b', 4], [2, 'a', 3], [2, 'b', 5], [3, 'a', 1], [3, 'b', 6], [4, 'a', 5], [4, 'b', 1], [5, 'a', 6], [5, 'b', 2], [6, 'a', 4], [6, 'b', 3]],
    "I": [1],
    "F": [1]
}

auto32 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4, 5, 6, 7],
    "transitions": [[1, 'a', 3], [1, 'b', 2], [2, 'a', 4], [2, 'b', 1], [3, 'a', 5], [3, 'b', 4], [4, 'a', 7], [4, 'b', 3], [5, 'a', 6], [5, 'b', 7], [6, 'a', 6], [6, 'b', 6], [7, 'a', 6], [7, 'b', 5]],
    "I": [1],
    "F": [2, 4, 6, 7]
}

auto33 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4, 5, 6, 7],
    "transitions": [[1, 'a', 2], [1, 'b', 3], [2, 'a', 2], [2, 'b', 4], [3, 'a', 5], [3, 'b', 1], [4, 'a', 5], [4, 'b', 7], [5, 'a', 5], [5, 'b', 6], [6, 'a', 2], [6, 'b', 7], [7, 'a', 7], [7, 'b', 7]],
    "I": [1],
    "F": [2, 4, 6, 7]
}

auto34 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4, 5],
    "transitions": [[1, 'a', 1], [1, 'a', 2], [2, 'a', 5], [2, 'b', 3], [3, 'a', 4], [3, 'b', 3], [5, 'b', 5]],
    "I": [1],
    "F": [4, 5]
}

# Automates TD 5 déterminisés
auto35 = {
    "alphabet": ['a', 'b', 'c'],
    "etats": [1, 2, 3, 4],
    "transitions": [[1, 'a', 2], [1, 'b', 1], [1, 'c', 1], [2, 'a', 2], [2, 'b', 3], [2, 'c', 2], [3, 'a', 2], [3, 'b', 1], [3, 'c', 4], [4, 'a', 4], [4, 'b', 4], [4, 'c', 4]],
    "I": [1],
    "F": [1]
}

auto36 = {
    "alphabet": ['a', 'b', 'c'],
    "etats": [1, 2, 3],
    "transitions": [[1, 'a', 1], [1, 'b', 2], [1, 'c', 3], [2, 'a', 2], [2, 'b', 3], [2, 'c', 3], [3, 'a', 3], [3, 'b', 3], [3, 'c', 3]],
    "I": [1],
    "F": [3]
}

auto37 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4, 5, 6, 7],
    "transitions": [[1, 'a', 2], [1, 'b', 4], [2, 'a', 2], [2, 'b', 3], [3, 'a', 5], [3, 'b', 4], [4, 'a', 7], [4, 'b', 6], [5, 'a', 2], [5, 'b', 3], [6, 'a', 5], [6, 'b', 4], [7, 'a', 7], [7, 'b', 7]],
    "I": [1],
    "F": [5, 6]
}

auto38 = {
    "alphabet": ['a', 'b'],
    "etats": [1, 2, 3, 4, 5],
    "transitions": [[1, 'a', 2], [1, 'b', 3], [2, 'a', 2], [2, 'b', 4], [3, 'a', 2], [3, 'b', 5], [4, 'a', 2], [4, 'b', 5], [5, 'a', 5], [5, 'b', 5]],
    "I": [1],
    "F": [4, 5]
}

# Automate TD 7 ex 1 haut gauche
auto39 = {
    "alphabet": ["a", "b"],
    "etats": [1, 2, 3, 4, 5, 6],
    "transitions": [[1, "a", 2], [1, "b", 2], [2, "a", 3], [2, "b", 4], [3, "a", 4], [4, "a", 3], [3, "b", 5], [4, "b", 6], [5, "a", 6], [5, "b", 5], [6, "b", 6], [6, "a", 5]],
    "I": [1],
    "F": [5, 6]
}

# Automate TD 7 ex 1 haut droite
auto40 = {
    "alphabet": ["a", "b"],
    "etats": [1, 2, 3, 4, 5, 6],
    "transitions": [[1, "a", 5], [1, "b", 4], [2, "a", 6], [2, "b", 6], [3, "a", 6], [3, "b", 3], [4, "a", 2], [4, "b", 1], [5, "a", 2], [5, "b", 3], [6, "a", 3], [6, "b", 6]],
    "I": [1],
    "F": [1, 2, 3, 6]
}

# Automate TD 7 ex 1 bas gauche
auto41 = {
    "alphabet": ["a", "b"],
    "etats": [1, 2, 3, 4, 5, 6],
    "transitions": [[1, "a", 2], [1, "b", 4], [2, "a", 3], [2, "b", 4], [3, "a", 3], [3, "b", 4], [4, "a", 5], [4, "b", 6], [5, "a", 5], [5, "b", 5], [6, "a", 5], [6, "b", 6]],
    "I": [1],
    "F": [5, 6]
}

# Automate TD 7 ex 1 bas droite
auto42 = {
    "alphabet": ["a", "b"],
    "etats": [1, 2, 3, 4, 5, 6, 7],
    "transitions": [[1, "a", 4], [1, "b", 2], [2, "a", 3], [2, "b", 7], [3, "a", 2], [3, "b", 5], [4, "a", 7], [4, "b", 7], [5, "a", 7], [5, "b", 6], [6, "a", 7], [6, "b", 5], [7, "a", 5], [7, "b", 7]],
    "I": [1],
    "F": [2, 4, 7]
}

# Automate TD 7 ex 2 question 1
auto43 = {
    "alphabet": ["a", "b"],
    "etats": [1, 2, 3, 4, 5],
    "transitions": [[1, "a", 2], [1, "b", 1], [2, "a", 1], [2, "b", 3], [3, "a", 4], [3, "b", 3], [4, "a", 3], [4, "b", 5], [5, "a", 5], [5, "b", 5]],
    "I": [1],
    "F": [5]
}

# Automate TD 7 ex 2 question 2
auto44 = {
    "alphabet": ["a", "b"],
    "etats": [1, 2],
    "transitions": [[1, "a", 1], [1, "b", 2], [2, "a", 1]],
    "I": [1],
    "F": [1, 2]
}