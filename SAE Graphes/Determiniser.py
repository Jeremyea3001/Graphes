from Utilitaire import Utilitaire

class Determiniser :

    @staticmethod
    def deterministe(auto: dict) -> bool :
        """
        Calcule si un automate est déterministe ou non.
        :param auto: Un automate quelconque
        :returns: True si l'automate passé en paramètre est déterministe et False sinon
        >>> from Automates import auto0, auto2
        >>> print(Determiniser.deterministe(auto0))
        True
        >>> print(Determiniser.deterministe(auto2))
        False
        """
        if len(auto["I"]) > 1 :
            return False
        etats = []
        for transition in auto["transitions"] :
            if (transition[0], transition[1]) not in etats :
                etats.append((transition[0], transition[1]))
                # Ajoute la paire (état, lettre) dans la liste etats si elle n'est pas dedans
            else :
                return False
                # Si la paire (état, lettre) est déjà dans la liste, l'automate n'est pas déterministe
                # et la fonction renvoie faux
        return True
        # Si aucune paire n'est en double, alors l'automate est déterministe
        # et la fonction renverra vrai


    def __destinations(auto: dict, etat: set[int]) -> dict :
        """
        Calcule les destinations possibles à partir d'un état déterminisé.
        :param auto: Un automate non déterminisé
        :param etat: Un état de l'automate déterminisé de auto
        :returns: Les destinations possibles à partir d'un état avec l'automate auto.
        """
        dico = {e: set() for e in auto["alphabet"]}
        # Dictionnaire avec comme clé les lettres de l'alphabet et valeur
        # la liste des destinations possibles à partir d'un état et un automate
        for transition in auto["transitions"] :
            if transition[0] in etat :
                # Si l'état de départ est dans la liste des états
                dico[transition[1]].add(transition[2])
                # Ajoute les états destinataires de la transition dans le dictionnaire
                # avec la lettre correspondante (pas de vérification pour des doublons car j'utilise un set)
        return dico


    # Attention ! Si etats est vide à l'appel de la fonction, resultat ne sera pas rempli.
    def __ajout_transitions(auto: dict, resultat: dict, etats: list[set[int]]) -> dict :
        """
        Calcule les transitions et les états de l'automate déterministe de auto et les ajoute dans resultat sur place.
        :param auto: Un automate quelconque
        :param resultat: Un automate vide, qui sera rempli après l'appel de la fonction
        :param etats: La liste des états où il faut calculer les destinations
        :returns: L'automate déterministe avec ses transitions et ses états
        """
        if not etats :
            return resultat
        # S'il n'y a plus d'états où calculer les destinations, renvoyer l'automate résultat
        # (condition d'arrêt de la fonction récursive)

        dico = Determiniser.__destinations(auto, etats[-1])
        # Dictionnaire avec comme clé les lettres de l'alphabet et en valeurs
        # la (ou les) état(s) destinataire(s) à partir du dernier état de la liste etats

        for key, value in dico.items() :

            if not value :
                continue
            # Si la liste d'états destinataires est vide, 
            # continuer dans la boucle

            if value not in resultat["etats"] and value not in etats :
                etats.insert(-2, value)
            # Si l'état calculé n'a pas encore été ajouté à l'automate résultat
            # et qu'il n'est pas non plus dans la liste des états où il faut calculer
            # ses destinations, l'ajouter dedans

            transition = [etats[-1], key, value]
            # Le format de la transition

            if transition not in resultat["transitions"] :
                resultat["transitions"].append(transition)
            # Si la transition n'est pas déjà dans l'automate, l'ajouter


        if etats[-1] not in resultat["etats"] :
            resultat["etats"].append(etats.pop())

        else :
            etats.pop()
        # Suppression de l'état qui a été utilisé à cet appel
        # (soit en l'ajoutatnt dans l'automate s'il n'est pas dedans
        #  soit juste en le supprimant de la liste etats)

        return Determiniser.__ajout_transitions(auto, resultat, etats)
        # Répéter cette fonction tant que la liste etats n'est pas vide
                
    @staticmethod
    def determinise(auto: dict) -> dict :
        """
        Calcule un automate déterministe.
        :param auto: Un automate quelconque
        :returns: L'automate déterministe de auto
        """
        resultat = {
                    "alphabet": Utilitaire.copie_liste(auto["alphabet"]),
                    "transitions": [],
                    "etats": [],
                    "I": [Utilitaire.copie_liste(auto["I"])],
                    "F": []
                    }
        
        if Determiniser.deterministe(auto) :
            return resultat
        # Si l'automate est déjà déterministe, renvoie l'automate initial

        Determiniser.__ajout_transitions(auto, resultat, [set(auto["I"])])
        # Ajout des transitions de l'automate déterministe

        for etat_final in auto["F"] :
            for etat in resultat["etats"] :
                if etat_final in etat and etat not in resultat["F"] :
                    resultat["F"].append(etat)
        # Si un état est final dans l'état déterministe,
        # le mettre en état final

        return resultat
    
if __name__ == "__main__" :
    import doctest
    doctest.testmod()