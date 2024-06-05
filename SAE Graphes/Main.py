# Les fonctions intermédiaires ont un __ devant leur nom
# (c'est une convention pour dire que cette fonction est privée)

# import Automates
# Ne contient que des automates prédéfinis (pour tester)

from Utilitaire import Utilitaire       # Quelques autres fonctions utiles
# Cette classe contient les fonctions defauto et renommage

from Langage import Langage
# Cette classe contient les fonctions de la première partie (excepté defauto qui est dans Utilitaire)

from Determiniser import Determiniser
# Cette classe contient les fonctions de la deuxième partie (excepté renommage qui est dans Utilitaire)

from Completer import Completer
# Cette classe contient les fonctions de la troisième partie

from Produits import Produits
# Cette classe contient les fonctions de la quatrième partie

from Fermeture import Fermeture
# Cette classe contient les fonctions de la cinquième partie

from Minimaliser import Minimaliser
# Cette classe contient les fonctions de la dernière partie


def main() -> None :
    """Fonction main"""
    auto0 = {
        "alphabet":['a', 'b'],
        "etats": [0, 1, 2, 3],
        "transitions":[[0, 'a', 1], [0, 'b', 3], [1, 'a', 0], [1, 'a', 2], [2, 'a', 0], [3, 'b', 0]], 
        "I":[0, 3],
        "F":[0]
    }
    auto_det = Determiniser.determinise(auto0)
    print("Automate déterminisé : ")
    print(auto_det)
    print("\nAvec les états renommés :")
    print(Utilitaire.renommage(auto_det))
    print("\n")
    
    auto1 = {
        "alphabet":['a', 'b'],
        "etats": [0, 1, 2, 3, 4, 5, 6, 7],
        "transitions":[[0, 'a', 1], [0, 'b', 2], [1, 'a', 3], [1, 'b', 1], [2, 'a', 4], [2, 'b', 2], [3, 'a', 5], [3, 'b', 3], [4, 'a', 2], [4, 'b', 4], [5, 'a', 6], [5, 'b', 1], [6, 'a', 7], [6, 'b', 2], [7, 'a', 6], [7, 'b', 7]], 
        "I":[0],
        "F":[1, 2, 3, 6]
    }
    auto_min = Minimaliser.minimise(auto1)
    print("Automate minimal : ")
    print(auto_min)
    print("\nAvec les états renommés :")
    print(Utilitaire.renommage(auto_min))
    print("\n")

    auto2 = {
        "alphabet":['a', 'b'],
        "etats": [0, 1, 2],
        "transitions":[[0, 'a', 1], [1, 'b', 2], [2, 'a', 2], [2, 'b', 2]], 
        "I":[0],
        "F":[2]
    }

    auto3 = {
        "alphabet":['a', 'b'],
        "etats": [0, 1],
        "transitions":[[0, 'a', 1], [0, 'b', 0], [1, 'a', 0], [1, 'b', 1]], 
        "I":[0],
        "F":[0]
    }
    auto_int = Produits.inter(auto2, auto3)
    print("Intersection des automates :")
    print(auto_int)
    print("\nAvec les états renommés :")
    print(Utilitaire.renommage(auto_int))

if __name__ == "__main__" :
    main()