# -*- coding: utf-8 -*-

class Piece:

    def __init__(

        self,
        couleur: str = "blanc",
        valeur: str = "Pion",
        type: bool = True,
        case_précédente: str = '',
    ):
        """Initialise une Pièce qui est une liste de 4 arguments

        Args:
            couleur (str, optional): 'blanc' ou 'noir''
            valeur (str, optional): 'Dame', 'Roi', Pion',...'
            type (bool, optional): True=pièce    False=cursor ou autre
            case_précédente (str, optional): la case occupée avant le dernier mouvement de cette pièce
        """
        self.couleur = couleur
        self.valeur = valeur
        self.type = type
        self.case_précédente=case_précédente

    def __str__(self):
        if self.type:
            return f"Piece   : {self.valeur} {self.couleur} qui vient de {self.case_précédente}"
        else:
            return f"Curseur : {self.valeur} {self.couleur} qui vient de {self.case_précédente}"
        
    @property
    def fichier(self):
        """Returns the file name of the picture of one piece"""
        return f"images\\{self.valeur.capitalize()}_{self.couleur.lower()}.png"
    
