from Utilitaire import Utilitaire

class Langage :

    @staticmethod
    def pref(mot: str) -> list[str] :
        """
        Calcule les préfixes d'un mot.
        :param mot: Un mot quelconque
        :returns: La liste des préfixes du mot
        >>> Langage.pref('coucou')
        ['', 'c', 'co', 'cou', 'couc', 'couco', 'coucou']
        >>> Langage.pref('')
        ['']
        >>> Langage.pref('a')
        ['', 'a']
        """
        return [mot[0: i] for i in range(len(mot) + 1)]

    @staticmethod
    def suf(mot: str) -> list[str] :
        """
        Calcule les suffixes d'un mot.
        :param mot: Un mot quelconque
        :returns: La liste des suffixes du mot
        >>> Langage.suf('coucou')
        ['coucou', 'oucou', 'ucou', 'cou', 'ou', 'u', '']
        >>> Langage.suf('')
        ['']
        >>> Langage.suf('a')
        ['a', '']
        """
        return [mot[i: len(mot)] for i in range(len(mot) + 1)]

    @staticmethod
    def fact(mot: str) -> list[str] :
        """
        Calcule les facteurs d'un mot.
        :param mot: Un mot quelconque
        :returns: La liste des facteurs du mot
        >>> Langage.fact('coucou')
        ['', 'c', 'co', 'cou', 'couc', 'couco', 'coucou', 'o', 'ou', 'ouc', 'ouco', 'oucou', 'uc', 'uco', 'ucou', 'u']
        >>> Langage.fact('')
        ['']
        >>> Langage.fact('a')
        ['', 'a']
        """
        lst = [""]
        for i in range(0, len(mot) + 1) :
            for j in range(i, len(mot) + 1) :
                if mot[i: j + i] not in lst :
                    lst.append(mot[i: j + i])
        return lst

    @staticmethod
    def miroir(mot: str) -> str :
        """
        Calcule le miroir d'un mot.
        :param mot: Un mot quelconque
        :returns: Le mot miroir
        >>> Langage.miroir('coucou')
        'uocuoc'
        >>> Langage.miroir('')
        ''
        >>> Langage.miroir('a')
        'a'
        """
        resultat = ""
        for e in reversed(mot) :
            resultat += e
        return resultat

    @staticmethod
    def concatene(l1: list[str], l2: list[str]) -> list[str] :
        """
        Calcule la concaténation de deux langages.
        :param l1: Un langage quelconque
        :param l2: Un langage quelconque
        :returns: La concaténation des deux langages
        >>> l1=['aa','ab','ba','bb']
        >>> l2=['a', 'b', '']
        >>> Langage.concatene(l1, l2)
        ['aaa', 'aab', 'baa', 'aa', 'aba', 'abb', 'bab', 'ab', 'bba', 'ba', 'bbb', 'bb']
        """
        resultat = []
        for e1 in l1 :
            for e2 in l2 :
                if e1 + e2 not in resultat :
                    resultat.append(e1 + e2)
                if e2 + e1 not in resultat :
                    resultat.append(e2 + e1)
        
        return resultat

    @staticmethod
    def puis(l: list[str], n = 0) -> list[str] :
        """
        Calcule la puissance d'un langage.
        :param l: Un langage quelconque
        :param n: Un entier positif
        :returns: Le langage l à la puissance n
        :raises AssertionError: Lève une erreur si n est strictement inférieur à 0
        >>> l1=['aa','ab','ba','bb']
        >>> Langage.puis(l1, 2)
        ['aaaa', 'aaab', 'abaa', 'aaba', 'baaa', 'aabb', 'bbaa', 'abab', 'abba', 'baab', 'abbb', 'bbab', 'baba', 'babb', 'bbba', 'bbbb']
        """
        assert n >= 0
        if n == 0 :
            return [""]
        if n == 1 :
            return l
        else :
            return Langage.concatene(l, Langage.puis(l, n - 1))

    # On ne peut pas calculer l'étoile d'un langage car ce langage est infini et pour représenter ce langage, il faudrait donc une liste de longueur infinie.

    @staticmethod
    def tousmot(l: list[str], n = 0) -> list[str] :
        """
        Calcule l'étoile d'un langage.
        :param l: Un langage quelconque
        :param n: Un entier positif
        :returns: L'étoile d'un langage pour tous les mots de longueur inférieur ou égal à n
        :raises AssertionError: Lève une erreur si n est strictement inférieur à 0
        >>> Langage.tousmot(['a', 'b'], 3)
        ['', 'a', 'b', 'aa', 'ab', 'ba', 'bb', 'aaa', 'aab', 'baa', 'aba', 'abb', 'bab', 'bba', 'bbb']
        """
        assert n >= 0

        resultat = ['']

        lst = l.copy()
        while any(len(mot) <= n for mot in lst) :
            for mot in lst :
                if len(mot) <= n :
                    resultat.append(mot)
            lst = Langage.concatene(lst, l)

        return resultat
    
    @staticmethod
    def lirelettre(transitions: list[int, str, int], etats: list[int], lettre: str) -> list[int] :
        """
        Donne la liste des états accessibles à partir d'un état de etats et en lisant la lettre.
        :param transitions: Une liste de transitions
        :param etats: Une liste d'états
        :param lettre: Une lettre
        :returns: Les états accessibles à partir d'un état et de la lettre
        >>> from Automates import auto
        >>> print(Langage.lirelettre(auto["transitions"], auto["etats"], 'a'))
        [2, 4]
        """
        return list({etat2 for etat, letter, etat2 in transitions if letter == lettre and etat in etats})
        # Parcoure toutes les transitions et renvoie la liste des états destinataires si la lettre
        # de la transition correspond à la lettre donnée et si l'état de départ est dans la liste des états
    
    @staticmethod
    def liremot(transitions: list[int, str, int], etats: list[int], mot: str) -> list[int] :
        """
        Donne la liste des états accessibles à partir d'un état de etats et en lisant le mot.
        :param transitions: Une liste de transitions
        :param etats: Une liste d'états
        :param lettre: Un mot
        :returns: Les états accessibles à partir d'un état et du mot
        >>> from Automates import auto
        >>> print(Langage.liremot(auto["transitions"], auto["etats"], 'aba'))
        [4]
        """
        resultat = Utilitaire.copie_liste(etats)
        for lettre in mot :
            resultat = Langage.lirelettre(transitions, resultat, lettre)
            if not resultat :       # Si la liste est vide, renvoyer directement la liste vide (pas très utile mais un peu)
                return resultat
        return resultat
    
    @staticmethod
    def accepte(auto: dict, mot: str) -> bool :
        """
        Détermine si un mot est accepté par un automate.
        :param auto: Un automate
        :param mot: Un mot
        :returns: True si le mot est accepté par l'automate, False sinon
        """
        return any(etat in auto["F"] for etat in Langage.liremot(auto["transitions"], auto["I"], mot))

    @staticmethod
    def langage_accept(auto: dict, n = 0) -> list[str] :
        """
        Calcule le langage accepté par l'automate pour tout les mots de longueur inférieure à n.
        :param auto: Un automate
        :param n: Un entier
        :returns: Le langage accepté par l'automate pour tout les mots de longueur inférieure à n
        """
        langage = []
        for mot in Langage.tousmot(auto["alphabet"], n) :
            if Langage.accepte(auto, mot) :
                langage.append(mot)
        return langage
    
    # On ne peut pas créer une fonction qui renvoie la totalité du langage accepté par un automate car
    # celui-ci est (dans la majeure partie des cas) un langage infini
    # (et donc c'est aussi pour la même raison que le langage infini)

if __name__ == "__main__" :
    import doctest
    doctest.testmod()