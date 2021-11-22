# -*- coding: utf-8 -*-
import random
from settings import COULEUR, VALEUR,NOM_PNG_VAL ,NOM_PNG_COU

class Piece:

    def __init__(

        self,
        couleur: int=0,
        valeur: int=0,
        case_précédente: str = '',
        case_coup_précédent: str=''
    ):
        """ Piece ou cursor

        Args:
            couleur (int, optional): 0=blanc, 1=noir
            valeur (int, optional): 0=roi, 1=dame, 2=fou, etc... Defaults to 0
            case_précédente (str, optional) : case où était la pièce avant son dernier mouvement
            case_coup_précédent (str, optional) : case où était la pièce juste avant le dernier coup joué
        """
        self.couleur = couleur
        self.valeur = valeur
        self.case_précédente=case_précédente
        self.case_coup_précédente=case_coup_précédent

    def __str__(self):
        return f"Piece   : {VALEUR[self.valeur][0]} {COULEUR[self.couleur][0]} qui vient de {self.case_précédente}"

        
    @property
    def fichier(self):
        """Returns the file name of the picture of one piece"""
        return f"images\\{NOM_PNG_VAL[self.valeur]}_{NOM_PNG_COU[self.couleur]}.png"

    
