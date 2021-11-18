# -*- coding: utf-8 -*-

class Piece:
    """Une Pièce"""

    def __init__(
        self,
        couleur: str = "blanc",
        valeur: str = "Pion",
        type: bool = True,                   # True= c'est une piece , False = c'est autrechose (un curseur, une marque, etc...)
        case_précédente: str = '',           # '' = la pièce n'a pas encore bougé , sinon 'A2' ou autre...
    ):
        """Initialise une Pièce

        Args:
            couleur (str, optional): blanc / noir                      . Defaults to 'blanc'.
            valeur (str, optional): pion,tour,cavalier,fou,dame,roi    . Defaults to 'pion'.
            ligne (str, optional): 1 à 8                               . Defaults to '2'.
            colonne (str, optional): A à H                             . Defaults to 'A'.
            type (str, optionnal) : text pour différencier les pieces des autres éventuelles marques (cursor, etc...)
        """
        self.couleur = couleur
        self.valeur = valeur
        self.type = type
        self.case_précédente=case_précédente

    def __str__(self):
        if self.type:
            return f"Piece   : {self.valeur} {self.couleur} était placé en {self.case_précédente}"
        else:
            return f"Curseur : {self.valeur} {self.couleur} était placé en {self.case_précédente}"
        
    @property
    def fichier(self):
        """Returns the file name of the picture of one piece"""
        return f"images\\{self.valeur.capitalize()}_{self.couleur.lower()}.png"
    
