from Utilitaire import Utilitaire

class Fermeture :

    @staticmethod
    def prefixe(auto: dict) -> dict :
        """
        Calcule un automate acceptant l'ensemble des prefixes des mots acceptés par un automate.
        :param auto: Un automate émondé
        :returns: L'automate acceptant l'ensemble des prefixes des mots acceptés par un automate
        """
        resultat = Utilitaire.copie_dico(auto)
        resultat["F"] = Utilitaire.copie_liste(resultat["etats"])
        # Tous les états de l'automate sont finaux
        return resultat

    @staticmethod
    def suffixe(auto: dict) -> dict :
        """
        Calcule un automate acceptant l'ensemble des suffixes des mots acceptés par un automate.
        :param auto: Un automate émondé
        :returns: L'automate acceptant l'ensemble des suffixes des mots acceptés par un automate
        """
        resultat = Utilitaire.copie_dico(auto)
        resultat["I"] = Utilitaire.copie_liste(resultat["etats"])
        # Tous les états de l'automate sont initiaux
        return resultat

    @staticmethod
    def facteur(auto: dict) -> dict :
        """
        Calcule un automate acceptant l'ensemble des facteurs des mots acceptés par un automate.
        :param auto: Un automate émondé
        :returns: L'automate acceptant l'ensemble des facteurs des mots acceptés par un automate
        """
        resultat = Utilitaire.copie_dico(auto)
        resultat["I"] = Utilitaire.copie_liste(resultat["etats"])
        resultat["F"] = Utilitaire.copie_liste(resultat["etats"])
        # Tous les états de l'automate sont à la fois initiaux et finaux 
        return resultat

    @staticmethod
    def miroir(auto: dict) -> dict :
        """
        Calcule un automate acceptant l'ensemble des miroirs des mots acceptés par un automate.
        :param auto: Un automate émondé
        :returns: L'automate acceptant l'ensemble des miroirs des mots acceptés par un automate
        """
        resultat = Utilitaire.copie_dico(auto)
        resultat["I"], resultat["F"] = resultat["F"], resultat["I"]
        # Les états initiaux sont échangés avec les états finaux
        for transition in resultat["transitions"] :
            transition[0], transition[2] = transition[2], transition[0]
        # Les transitions sont inversées
        # (l'état de départ devient l'état destinataire et vice versa)
        return resultat