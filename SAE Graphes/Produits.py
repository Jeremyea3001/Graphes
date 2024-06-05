from Completer import Completer

class Produits :

    # La différence entre destinations (la fonction pour déterminiser) et destination (la fonction en dessous)
    # est que destination n'a qu'1 seule destination par lettre (donc juste un int) contrairement à destinations qui peut en
    # avoir plusieurs (donc une liste).
    # Faire une autre fonction pour les automates produits est meilleur à mon avis car
    # je n'aurai pas à travailler avec une liste contenant qu'une seule valeur dedans

    def __destination(auto: dict, etat: int) -> dict :
        """
        Calcule les destinations possibles à partir d'un état à l'aide d'un automate déterministe.
        :param auto: Un automate déterministe
        :param etat: Un état de l'automate déterministe
        :returns: Les lettres en clé avec leur destination en valeur
        """
        dico = {lettre: None for lettre in auto["alphabet"]}
        # Dictionnaire avec comme clé toutes les lettres de l'alphabet de l'automate
        # et en valeur l'état destinataire à partir de l'état donné en paramètre
        for transition in auto["transitions"] :
            if transition[0] == etat :
                dico[transition[1]] = transition[2]
        # Ajoute l'état destinataire dans le dictionnaire (s'il existe)
        return dico


    def __ajout_transitions_produit(auto1: dict, auto2: dict, resultat: dict, etats: list[tuple]) -> dict :
        """
        Calcule l'automate déterministe du produit de deux automates.
        :param auto1: Un automate déterministe
        :param auto2: Un automate déterministe
        :param resultat: L'automate où ajouter les transitions
        :param etats: La liste des états où leurs destinations n'ont pas encore été calculées
        :returns: L'automate produit déterministe
        """
        if not etats :
            return resultat
        # Si la liste etats est vide, renvoie l'automate résultat
        # (condition d'arrêt de la fonction récursive)

        dico1 = Produits.__destination(auto1, etats[-1][0])
        dico2 = Produits.__destination(auto2, etats[-1][1])
        # Calcul des destinations des 2 états de l'état produit

        for lettre in resultat["alphabet"] :
            if dico1[lettre] is None or dico2[lettre] is None :
                continue
            # Si l'une des destinations n'existe pas,
            # passer à la prochaine lettre de l'alphabet

            etat_produit = (dico1[lettre], dico2[lettre])
            # Format de l'état produit

            transition = [etats[-1], lettre, etat_produit]
            # Format de la transition

            if transition not in resultat["transitions"] :
                resultat["transitions"].append([etats[-1], lettre, etat_produit])
            # Si la transition n'a pas encore été ajouté dans l'automate resultat,
            # elle est ajoutée

            if etat_produit not in resultat["etats"] and etat_produit not in etats :
                etats.insert(-2, etat_produit)
            # Si l'état produit n'est pas dans l'automate resultat et s'il n'est pas déjà dans
            # la liste des états où les destinations sont à calculer,
            # l'état produit est ajouté dans celle-ci


        if etats[-1] not in resultat["etats"] :
            resultat["etats"].append(etats.pop())

        else :
            etats.pop()
        # Suppression de l'état utilisé lors de cet appel de la fonction
        # (soit en l'ajoutant dans l'automate résultat
        #  soit juste en le supprimant de la liste etats)

        return Produits.__ajout_transitions_produit(auto1, auto2, resultat, etats)
        # Répète cette fonction jusqu'à ce que la liste etats soit vide

    @staticmethod
    def inter(auto1: dict, auto2: dict) -> dict :
        """
        Calcule l'intersection de 2 automates déterministes.
        :param auto1: Un automate déterministe
        :param auto2: Un automate déterministe
        :returns: L'intersection des 2 automates
        >>> from Automates import auto4, auto5
        >>> print(Produits.inter(auto4,auto5))
        {'alphabet': ['a', 'b'], 'etats': [(0, 0), (1, 0), (2, 1), (2, 2), (2, 0)], 'transitions': [[(0, 0), 'a', (1, 0)], [(1, 0), 'b', (2, 1)], [(2, 1), 'a', (2, 1)], [(2, 1), 'b', (2, 2)], [(2, 2), 'a', (2, 2)], [(2, 2), 'b', (2, 0)], [(2, 0), 'a', (2, 0)], [(2, 0), 'b', (2, 1)]], 'I': [(0, 0)], 'F': [(2, 1), (2, 0)]}
        """
        resultat = {
            "alphabet": auto1["alphabet"],
            "etats": [],
            "transitions": [],
            "I": [(auto1["I"][0], auto2["I"][0])],
            "F": [],
        }

        Produits.__ajout_transitions_produit(auto1, auto2, resultat, [(auto1["I"][0], auto2["I"][0])])
        # Ajoute les transitions de l'automate produit dans resultat

        for etat in resultat["etats"] :
            if etat[0] in auto1["F"] and etat[1] in auto2["F"] :
                resultat["F"].append(etat)
        # Ajoute les états finaux de l'automate produit dans resultat
        # (Si l'état en première position est un état final d'auto1 et si l'état en deuxième position est un état final d'auto2)

        return resultat

    @staticmethod
    def difference(auto1: dict, auto2: dict) -> dict :
        """
        Calcule la différence L(A1) \ L(A2) où A1 et A2 sont des automates déterministes.
        :param auto1: Un automate déterministe
        :param auto2: Un automate déterministe
        :returns: L'automate acceptant L(A1) \ L(A2)
        """
        auto1_complet = Completer.complete(auto1)
        auto2_complet = Completer.complete(auto2)
        # Complète les 2 automates s'ils ne sont pas complets

        resultat = {
            "alphabet": auto1["alphabet"],
            "etats": [],
            "transitions": [],
            "I": [(auto1["I"][0], auto2["I"][0])],
            "F": []
        }

        Produits.__ajout_transitions_produit(auto1_complet, auto2_complet, resultat, [(auto1_complet["I"][0], auto2_complet["I"][0])])
        # Ajoute les transitions de l'automate produit dans resultat
        
        for etat in resultat["etats"] :
            if etat[0] in auto1_complet["F"] and etat[1] not in auto2_complet["F"] :
                resultat["F"].append(etat)
        # Ajoute les états finaux de l'automate produit
        # (Si l'état en première position est un état final d'auto1 et si l'état en deuxième position n'est pas un état final d'auto2)

        return resultat
    
if __name__ == "__main__" :
    import doctest
    doctest.testmod()