# -*- coding: utf-8 -*-

from class_echiquier import Echiquier


class Partie:
    def __init__(self, echiquier=Echiquier('blanc'), liste_de_coups=[]):
        """un Partie est constituée d'un échiquier de départ (donc une liste de Pièces)
           et d'une liste de coups.

        Args:
            echiquier ([type]): voir classe échiquier
            liste_de_coups ([type]): listee de string du type "E2E4"
        """
        self.echiquier=echiquier
        self.liste_de_coups=liste_de_coups
        

            
        
