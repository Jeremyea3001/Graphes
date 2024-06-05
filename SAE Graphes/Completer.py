from Utilitaire import Utilitaire
from Determiniser import Determiniser


class Completer :
    
    def __creation_dico_a_complete(auto: dict) -> dict :
        """
        Crée un dictionnaire avec comme clé les lettres de l'alphabet de l'automate et comme valeurs la liste des états où il manque la transition avec la lettre en clé dans l'automate.
        :param auto: Un automate quelconque
        :returns: Le dictionnaire 
        """
        dico = {lettre : auto["etats"].copy() for lettre in auto["alphabet"]}
        # Crée un dictionnaire avec comme clé toutes les lettres de l'alphabet et les valeurs tous les états de l'automate.
        for transition in auto["transitions"] :
            if transition[0] in dico[transition[1]] :
                dico[transition[1]].remove(transition[0])
        # Enlève du dictionnaire tout les états qui ont une transition partant de lui
        return dico

    @staticmethod
    def complet(auto: dict) -> bool :
        """
        Détermine si l'automate est complet ou non
        :param auto: Un automate quelconque
        :returns: Un booléen qui indique si l'automate est complet
        >>> from Automates import auto0, auto1
        >>> Completer.complet(auto0)
        False
        >>> Completer.complet(auto1)
        True
        """
        dico = Completer.__creation_dico_a_complete(auto)
        return all(not v for v in dico.values())
        # Si toutes les valeurs du dictionnaire de la fonction est une liste vide, alors la fonction renverra vrai
        # (car cela voudrait dire qu'il manque aucune transitions pour tous les états)
        # sinon, elle renverra faux

    @staticmethod
    def complete(auto: dict) -> dict :
        """
        Calcule un automate complet de auto et, si ce n'est pas le cas, le déterminise aussi.
        :param auto: Un automate quelconque
        :returns: L'automate complété et déterministe
        >>> from Automates import auto0
        >>> print(Completer.complete(auto0))
        {'alphabet': ['a', 'b'], 'etats': [0, 1, 2, 3, 4], 'transitions': [[0, 'a', 1], [1, 'a', 1], [1, 'b', 2], [2, 'a', 3], [3, 'a', 4], [4, 'a', 4], [0, 'b', 4], [2, 'b', 4], [3, 'b', 4], [4, 'b', 4]], 'I': [0], 'F': [3]}
        """
        resultat = Utilitaire.copie_dico(auto)

        if not Determiniser.deterministe(resultat) :
            resultat = Utilitaire.renommage(Determiniser.determinise(resultat))
        # Si l'automate n'est pas déterministe, la fonction le déterminise
            
        if Completer.complet(resultat) :
            return resultat
        # Si l'automate est déjà complet, la fonction renvoie directement l'automate de base

        dico = Completer.__creation_dico_a_complete(resultat)

        etat_vide = max(resultat["etats"]) + 1
        # Le nom de l'état pour l'ensemble vide

        resultat["etats"].append(etat_vide)
        for lettre, etats in dico.items() :

            for etat in etats :
                resultat["transitions"].append([etat, lettre, etat_vide])
                # Rajoute les transitions vers l'état supplémentaire dans le résultat

            resultat["transitions"].append([etat_vide, lettre, etat_vide])
            # Rajoute les boucles sur l'état pour l'ensemble vide

        return resultat

    @staticmethod
    def complement(auto: dict) -> dict :
        """
        Calcule le complément d'un automate.
        :param auto: Un automate quelconque
        :returns: Le complément de l'automate
        >>> from Automates import auto3
        >>> print(Completer.complement(auto3))
        {'alphabet': ['a', 'b'], 'transitions': [[0, 'a', 1], [1, 'a', 1], [1, 'b', 2], [2, 'b', 2], [2, 'a', 3], [3, 'a', 3], [0, 'b', 3], [3, 'b', 3]], 'etats': [0, 1, 2, 3], 'I': [0], 'F': [0, 1, 3]}
        """
        if not Completer.complet(auto) :
            resultat = Completer.complete(auto)
        else :
            resultat = Utilitaire.copie_dico(auto)

        etat_finaux = [etat for etat in resultat["etats"] if etat not in resultat["F"]]
        # Liste qui contiendra les états qui ne sont pas finaux dans l'automate

        resultat["F"] = etat_finaux
        # Remplace la liste des états finaux de l'automate initial par ceux qui ne le sont pas

        return resultat

if __name__ == "__main__" :
    import doctest
    doctest.testmod()