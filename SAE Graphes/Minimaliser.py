from Utilitaire import Utilitaire
from Determiniser import Determiniser
from Completer import Completer

class Minimaliser :

    @staticmethod
    def __donne_transitions_utiles(auto: dict, classe: list[int]) -> dict :
        """
        Crée un dictionnaire de transitions sous la forme : { etatDepart : { lettre : etatArrivée }}.
        Ne prend en compte uniquement les états dans la classe.
        :param auto: Un automate quelconque
        :param classe: La classe sur laquelle se baser pour les transitions
        :returns: Le dictionnaire de transitions
        """
        resultat = {etat : dict() for etat in classe}

        for transition in auto["transitions"] :

            if transition[0] in classe :
                resultat[transition[0]][transition[1]] = transition[2]

        return resultat

    @staticmethod
    def __test_equivalence(etat1: int, etat2: int, classes: list[list[int]], transitions: dict, alphabet: list[str]) -> list[int, list[int]] : 
        """
        Détermine si 2 états sont dans la même classe d'équivalence k + 1.
        :param etat1: Le premier état à comparer
        :param etat2: Le deuxième état à comparer
        :param classes: La liste des classes d'équivalence au niveau k
        :param transitions: Le dictionnaire des transitions donné par la fonction donne_transitions_utiles
        :param alphabet: L'alphabet de l'automate
        :returns: True si les deux états sont dans la même classe d'équivalence, False sinon
        """
        for lettre in alphabet :

            for classe in classes :

                if transitions[etat1][lettre] in classe :

                    if transitions[etat2][lettre] in classe :
                        break       # Permet de continuer la boucle pour la prochaine lettre (ou si toutes les lettres ont été parcouru, de terminer les boucles et renvoyer True)
                    return False
                # Si une seule condition est vraie, les deux états n'appartiennent pas à la même classe d'équivalence

                elif transitions[etat2][lettre] in classe :
                    return False
                
                # Si aucune des deux conditions sont vraies, on continue pour les prochaines classes d'équivalence

        return True

    def __prochaine_classe_equivalence(auto: dict, classes: list[list[int]]) -> list[list[int]] :
        """
        Calcule les classes d'équivalence de tous les états d'un automate au niveau k + 1.
        :param auto: Un automate complet et déterministe
        :param classes: La classe d'équivalence des états de l'automate au niveau k
        :returns: Les classes d'équivalence de tous les états de l'automate au niveau k + 1  
        """
        resultat = []
        ajoute = False
        
        for classe in classes :

            # Si la classe n'a que 1 état, directement ajouter l'état au résultat et continuer dans la boucle
            if len(classe) == 1 :
                resultat.append(Utilitaire.copie_liste(classe))

            else :
                resultat.append([classe[0]])
                # Ajoute et crée une autre classe d'équivalence au résultat

                transitions_utiles = Minimaliser.__donne_transitions_utiles(auto, classe)

                for i in range(len(classe)) :
                # Parcoure tous les états de la classe actuelle

                    etat = classe[i]

                    for classe_courante in resultat :
                        if classe_courante[0] in classe : 
                            if Minimaliser.__test_equivalence(classe_courante[0], etat, classes, transitions_utiles, auto["alphabet"]) and etat not in classe_courante:
                    # Vérifie pour toutes les classes d'équivalence déjà calculées, si l'état de la classe sur laquelle on itère et un état de la classe d'équivalence du résultat appartiennent
                    # à la même classe d'équivalence et qu'il n'est pas déjà dans cette classe

                                classe_courante.append(etat)
                                ajoute = True
                                break
                                # Si la condition est vraie, ajoute l'état dans la classe où il appartient et sort de la boucle pour cet état

                    if not ajoute and [etat] not in resultat :
                        resultat.append([etat])
                    # Si l'état de la classe sur laquelle on itère n'a pas été ajouté (not ajoute), et que la classe d'équivalence avec l'état n'est pas déjà dans le résultat (pour le premier élément),
                    # crée une autre classe d'équivalence et l'ajoute au résultat

                    ajoute = False
                    # Réinitialise le booléen pour le prochain état de la boucle
        
        return resultat

    def __classe_max(auto: dict, classe1: list[list[int]], classe2: list[list[int]]) -> list[list[int]] :
        """
        Fonction récursive qui a comme condition d'arrêt l'égalité entre classe1 et classe2.
        :param auto: Un automate complet et déterministe
        :param classe1: La classe d'équivalence au niveau k
        :param classe2: La classe d'équivalence au niveau k + 1
        :returns: La classe d'équivalence au niveau k + 1 où elle est égale à celle du niveau k
        """
        if classe1 == classe2 :
            return classe1
        else :
            return Minimaliser.__classe_max(auto, classe2, Minimaliser.__prochaine_classe_equivalence(auto, classe2))

    def __creation_automate(auto: dict, classes: list[list[int]]) -> dict :
        """
        Crée l'automate minimale à partir de la classe d'équivalence maximale.
        :param auto: Un automate complet et déterministe
        :param classes: La classe d'équivalence maximale de l'automate
        :returns: L'automate minimale
        """
        resultat = {
            "alphabet" : Utilitaire.copie_liste(auto["alphabet"]),
            "etats" : Utilitaire.copie_liste(classes),
            "transitions" : [],
            "I" : [classe for classe in classes if auto["I"][0] in classe],
            "F" : []
        }

        # Transitions
        for transition in auto["transitions"] :
            transition_a_ajoute = [0, 0, 0]
            for classe in classes :

                if transition[0] in classe :
                    transition_a_ajoute[0] = classe
                    transition_a_ajoute[1] = transition[1]

                if transition[2] in classe :
                    transition_a_ajoute[2] = classe
                    transition_a_ajoute[1] = transition[1]

            if transition_a_ajoute not in resultat["transitions"] :
                resultat["transitions"].append(transition_a_ajoute)
        # Ajoute les transitions avec les nouveaux états au résultat

        # États finaux
        for classe in classes :
            if classe[0] in auto["F"] :
                resultat["F"].append(classe)
        # Ajoute les nouveaux états finaux au résultat

        return resultat

    @staticmethod
    def minimise(auto: dict) -> dict :
        """
        Calcule l'automate minimalisé de auto.
        :param auto: Un automate complet et déterministe
        :returns: L'automate minimalisé
        >>> from Automates import auto6
        >>> print(Minimaliser.minimise(auto6))
        {'alphabet': ['a', 'b'], 'etats': [[3], [4], [0], [1, 2, 5]], 'transitions': [[[0], 'a', [4]], [[0], 'b', [3]], [[1, 2, 5], 'a', [1, 2, 5]], [[1, 2, 5], 'b', [1, 2, 5]], [[3], 'a', [1, 2, 5]], [[3], 'b', [0]], [[4], 'a', [1, 2, 5]], [[4], 'b', [1, 2, 5]]], 'I': [[0]], 'F': [[0], [1, 2, 5]]}
        """
        if not Completer.complet(auto) :
            auto = Completer.complete(auto)
        classe_equivalence_0 = [[etat for etat in auto["etats"] if etat not in auto["F"]], Utilitaire.copie_liste(auto["F"])]
        classe_equivalence_max = Minimaliser.__classe_max(auto, classe_equivalence_0, Minimaliser.__prochaine_classe_equivalence(auto, classe_equivalence_0))
        return Minimaliser.__creation_automate(auto, classe_equivalence_max)
    
if __name__ == "__main__" :
    import doctest
    doctest.testmod()