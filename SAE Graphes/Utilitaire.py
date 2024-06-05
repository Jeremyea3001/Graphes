class Utilitaire :

    @staticmethod
    def copie_liste(L: list[any]) -> list[any] :
        """
        Crée une copie complète d'une liste
        :param L: Une liste
        :returns: La copie de la liste
        """
        lst = []
        for e in L :
            if type(e) == list :
                lst.append(Utilitaire.copie_liste(e))
            else :
                lst.append(e)
        return lst

    @staticmethod
    def copie_dico(dico: dict) -> dict :
        """
        Crée une copie complète d'un dictionnaire
        :param dico: Un dictionnaire
        :returns: La copie du dictionnaire
        """
        dico_copie = dict()
        for k, v in dico.items() :
            if type(v) == list :
                dico_copie[k] = Utilitaire.copie_liste(v)
            else :
                dico_copie[k] = v
        # On n'a pas besoin de vérifier si la clé est une liste car les clés
        # ne peuvent pas être mutables
        return dico_copie

    @staticmethod
    def defauto() -> dict :
        """
        Crée et formatte un automate avec des valeurs saisies.
        :returns: Un automate avec les valeurs saisies dans la fonction
        """
        resultat = {
                    "alphabet" : [],
                    "etats" : [],
                    "transitions" : [],
                    "I" : [],
                    "F" : []
                    }
        
        print("""Saisissez l'alphabet de l'automate
Tapez 'continue' pour continuer et 'quit' pour quitter la saisie de l'automate""")
        saisie = input()
        while saisie != "continue" :
            if saisie == "quit" :
                return None
            elif saisie in resultat["alphabet"] :
                print("Cette lettre est déjà dans la liste")
            else :
                resultat["alphabet"].append(saisie)
            saisie = input()

        print("""Saisissez les états de l'automate
Tapez 'continue' pour continuer et 'quit' pour quitter la saisie de l'automate""")  # Un état doit être un chiffre
        saisie = input()
        while saisie != "continue" :
            if saisie == "quit" :
                return None
            elif saisie in resultat["etats"] :
                print("Cet état est déjà dans la liste")
            else :
                if saisie.isdigit() :
                    resultat["etats"].append(saisie)
                else :
                    print("Le nom d'un état doit être un nombre")
            saisie = input()

        print("""Saisissez les transitions de l'automate dans le format : état1 lettre état2 (ex : 1 a 2)
Tapez 'continue' pour continuer et 'quit' pour quitter la saisie de l'automate""")
        saisie = input()
        while saisie != "continue" :
            if saisie == "quit" :
                return None
            else :
                saisie = saisie.split()
                if saisie in resultat["transitions"] :
                    print("Cette transition est déjà dans la liste")
                elif len(saisie) != 3 :
                    print(f"Le format de la transition est incorrecte, elle doit être sous la forme : {resultat['etats'][0]} {resultat['alphabet'][0]} {resultat['etats'][0]}")
                elif not (saisie[0] in resultat["etats"] and saisie[2] in resultat["etats"]) :
                    print(f"Un état saisi dans la transition n'est pas dans la liste des états\nLa liste d'états saisie est : {resultat['etats']}")
                elif saisie[1] not in resultat["alphabet"] :
                    print(f"La lettre saisie n'est pas dans l'alphabet\nL'alphabet saisi précédemment est : {resultat['alphabet']}")
                else :
                    resultat["transitions"].append(saisie)
            saisie = input()

        print("""Saisissez les états initiaux de l'automate
Tapez 'continue' pour continuer et 'quit' pour quitter la saisie de l'automate""")
        saisie = input()
        while saisie != "continue" :
            if saisie == "quit" :
                return None
            elif saisie in resultat["etats"] :
                if saisie not in resultat["I"] :
                    resultat["I"].append(saisie)
                else :
                    print("L'état saisi est déjà un état initial")
            else :
                print("L'état saisi n'est pas dans la liste des états")
            saisie = input()

        print("""Saisissez les états finaux de l'automate
Tapez 'continue' pour continuer et 'quit' pour quitter la saisie de l'automate""")
        saisie = input()
        while saisie != "continue" :
            if saisie == "quit" :
                return None
            elif saisie in resultat["etats"] :
                if saisie not in resultat["F"] :
                    resultat["F"].append(saisie)
                else :
                    print("L'état saisi est déjà un état final")
            else :
                print("L'état saisi n'est pas dans la liste des états")
            saisie = input()
        
        # Transtypage de tous les états en int.

        for i in range(len(resultat["etats"])) :
            resultat["etats"][i] = int(resultat["etats"][i])

        for i in range(len(resultat["I"])) :
            resultat["I"][i] = int(resultat["I"][i])

        for i in range(len(resultat["F"])) :
            resultat["F"][i] = int(resultat["F"][i])

        for e in resultat["transitions"] :
            e[0] = int(e[0])
            e[2] = int(e[2])

        return resultat

    @staticmethod
    def renommage(auto: dict) -> dict :
        """
        Renomme les états d'un automate avec des noms d'état composé.
        :param auto: Un automate avec des noms d'états composés
        :returns: L'automate avec les états renommés
        >>> from Determiniser import Determiniser
        >>> import Automates
        >>> print(Utilitaire.renommage(Determiniser.determinise(Automates.auto2)))
        {'alphabet': ['a', 'b'], 'transitions': [[0, 'a', 1], [1, 'a', 1], [1, 'b', 2], [2, 'a', 2], [2, 'b', 2]], 'etats': [0, 1, 2], 'I': [0], 'F': [1, 2]}
        """
        if type(auto["etats"][0]) != list and type(auto["etats"][0]) != set and type(auto["etats"][0]) != tuple :
            return auto
        resultat = Utilitaire.copie_dico(auto)

        dico = {tuple(etat) : i for i, etat in enumerate(auto["etats"])}
        # Création du dictionnaire avec comme clé les états (en tuple car une liste est mutable)
        # et en valeur un nombre qui incrémente

        # La fonction enumerate renvoie un tuple :
        # - la première valeur est l'indice de la deuxième valeur
        # - la deuxième valeur est la valeur à l'indice de la première valeur
        # Soit, la fonction renvoie un objet qui contient (dans ce cas) : (i, etats[i])
        # où etats est la liste des états (auto["etats"])

        for i in range(len(resultat["etats"])) :
            resultat["etats"][i] = dico[tuple(auto["etats"][i])]
        
        for e in resultat["transitions"] :
            for j in range(0, 3, 2) :
            # Boucle qui n'a comme valeur que 0 et 2 (car le pas est 2)
                e[j] = dico[tuple(e[j])]

        for i in range(len(resultat["I"])) :
            resultat["I"][i] = dico[tuple(auto["I"][i])]

        for i in range(len(resultat["F"])) :
            resultat["F"][i] = dico[tuple(auto["F"][i])]

        return resultat
    
if __name__ == "__main__" :
    import doctest
    doctest.testmod()