# -*- coding: utf-8 -*-
from src.moves import newCase

class Piece:
    """Une Pièce"""

    def __init__(
        self,
        couleur: str = "blanc",
        valeur: str = "Pion",
        colonne: str = "A",
        ligne: str = "2",
        type: str = "piece",                # par oppisition à cursor ou autre
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
        self.colonne = colonne
        self.ligne = ligne
        self.type = type
        self.case_précédente=case_précédente

    def __str__(self):
         return f"{self.valeur} {self.couleur} placé en {self.colonne}{self.ligne}"
    
    @property
    def fichier(self):
        """Returns the file name of the picture of one piece"""
        return f"images\\{self.valeur.capitalize()}_{self.couleur.lower()}.png"
    
    @property
    def case(self):
        """Retourne la case sous forme E2"""
        return self.colonne+self.ligne
    
    @property
    def coups_possibles(self):
        """Ici on gère les mouvements possibles d'une pièce sans soucis des autres pièces

        Returns:
            Liste de coups = ['A2',A4',...]
        """
        liste_coups=[]
        # ROI ------------------------------------------------------------------------------------------------
        if self.valeur=='Roi':
            for delta_col in (-1,0,1):
                for delta_lig in (-1,0,1):
                    new_coup=newCase(self.case,delta_col,delta_lig)
                    if new_coup!='' and new_coup not in liste_coups:
                        liste_coups.append(new_coup)
            if (self.case_précédente=='') and ((self.couleur=='blanc' and self.case=='E1') or (self.couleur=='noir' and self.case=='E8')):
                # condition nécessaire mais pas suffisante pour proposer un roque
                new_coup=newCase(self.case,2,0)
                liste_coups.append(new_coup)
                new_coup=newCase(self.case,-2,0)
                liste_coups.append(new_coup)
        # DAME ------------------------------------------------------------------------------------------------        
        if self.valeur=='Dame':
            for delta in range(-8,8):
                new_coup=newCase(self.case,delta,0)
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)        
                new_coup=newCase(self.case,0,delta)
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)
                new_coup=newCase(self.case,delta,delta)
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)
                new_coup=newCase(self.case,delta,-delta)
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)   
         # TOUR ------------------------------------------------------------------------------------------------        
        if self.valeur=='Tour':
            for delta in range(-8,8):
                new_coup=newCase(self.case,delta,0)
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)        
                new_coup=newCase(self.case,0,delta)
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)
        # FOU ------------------------------------------------------------------------------------------------        
        if self.valeur=='Fou':
            for delta in range(-8,8):
                new_coup=newCase(self.case,delta,delta)
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)
                new_coup=newCase(self.case,delta,-delta)
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)
        # CAVALIER ------------------------------------------------------------------------------------------------        
        if self.valeur=='Cavalier':
            for delta_lig in (-2,2):
                for delta_col in (-1,1):
                    new_coup=newCase(self.case,delta_col,delta_lig)
                    if new_coup!='' and new_coup not in liste_coups:
                        liste_coups.append(new_coup)
                    new_coup=newCase(self.case,delta_lig,delta_col)
                    if new_coup!='' and new_coup not in liste_coups:
                        liste_coups.append(new_coup)
         # PION ------------------------------------------------------------------------------------------------        
        if self.valeur=='Pion':
            if self.couleur=='blanc':
                new_coup=newCase(self.case,0,1)
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)
                new_coup=newCase(self.case,1,1)     # Prise Piece
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)
                new_coup=newCase(self.case,-1,1)     # Prise Piece
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)
                if self.ligne=='2':
                    new_coup=newCase(self.case,0,2)
                    if new_coup!='' and new_coup not in liste_coups:
                        liste_coups.append(new_coup)                    
            else:
                new_coup=newCase(self.case,0,-1)
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)
                new_coup=newCase(self.case,1,-1)     # Prise Piece
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)
                new_coup=newCase(self.case,-1,-1)     # Prise Piece
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)
                if self.ligne=='7':
                    new_coup=newCase(self.case,0,-2)
                    if new_coup!='' and new_coup not in liste_coups:
                        liste_coups.append(new_coup)                    
                              
        return liste_coups   

