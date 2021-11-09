# -*- coding: utf-8 -*-

class Piece:
    """Une Pièce
    """
    def __init__(self, couleur: str='blanc', valeur: str='pion', ligne: str='2', colonne: str='A'):
        """Initialise une Pièce

        Args:
            couleur (str, optional): blanc / noir                      . Defaults to 'blanc'.
            valeur (str, optional): pion,tour,cavalier,fou,dame,roi    . Defaults to 'pion'.
            ligne (str, optional): 1 à 8                               . Defaults to '2'.
            colonne (str, optional): A à H                             . Defaults to 'A'.
        """
        self.couleur = couleur
        self.valeur = valeur
        self.ligne = ligne
        self.colonne = colonne
        
    def __str__(self):
        print (self.valeur,' ',self.couleur,', placé en ',self.colonne, self.ligne)
    
        
        
