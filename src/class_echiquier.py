# -*- coding: utf-8 -*-
from PIL import Image
from src.class_piece import Piece
from src.moves import newCase

class Echiquier:
    def __init__(self, couleur_joueur: str = "blanc"):
        """Un Echiquier est une liste de Piece

        Args:
            echiquier (Piece): liste de Piece
        """
        if couleur_joueur in {"blanc", "noir"}:
            self.echiquier = self.new_game(couleur_joueur)
        else:
            self.echiquier = []

    def new_game(self, couleur_joueur: str = "blanc"):
        """Creates a new game for player couleur_joueur

        Args:
            couleur_joueur = 'blanc' ou 'noir' à mettre en bas de l'echiquier
        """
        self.echiquier = []
        col = couleur_joueur
        lig = self._extracted_from_new_game("1", col, "2")
        col = "noir" if col == "blanc" else "blanc"
        lig = self._extracted_from_new_game("8", col, "7")
        return self.echiquier

    # To save typing parts for new_game twice
    def _extracted_from_new_game(self, arg0, col, ligne):
        result = arg0
        self.echiquier.append(Piece(col, valeur="Roi", colonne="E", ligne=result))
        self.echiquier.append(Piece(col, valeur="Dame", colonne="D", ligne=result))
        self.echiquier.append(Piece(col, valeur="Fou", colonne="C", ligne=result))
        self.echiquier.append(Piece(col, valeur="Fou", colonne="F", ligne=result))
        self.echiquier.append(Piece(col, valeur="Cavalier", colonne="B", ligne=result))
        self.echiquier.append(Piece(col, valeur="Cavalier", colonne="G", ligne=result))
        self.echiquier.append(Piece(col, valeur="Tour", colonne="A", ligne=result))
        self.echiquier.append(Piece(col, valeur="Tour", colonne="H", ligne=result))
        for c in "ABCDEFGH":
            self.echiquier.append(Piece(col, valeur="Pion", colonne=c,ligne=ligne))

        return result

    def trace(self):
        """Trace le plateau de jeu

        Returns:
            image]: plateau avec ses pièces et ses éventuels curseurs
        """
        PLATEAU = Image.open("images\\échiquier.jpg")
        image_new = Image.new("RGB", (PLATEAU.width, PLATEAU.height))
        image_new.paste(PLATEAU, (0, 0))
        for p in self.echiquier:
            figurine = Image.open(p.fichier)
            c = int(198 + "ABCDEFGH".find(p.colonne) * 288)
            l = int(2210 - "12345678".find(p.ligne) * 288)
            image_new.paste(figurine, (c, l), figurine)

        # image_new.save('images\\mergedImages.png')
        return image_new

    def cleanCursor(self):
        """Ne conserve que les pièces de l'échiquier (retire les cursors)"""
        l = [p for p in self.echiquier if p.type == "piece"]
        self.echiquier = l
        return

    def ma_case(self, x, y):
        col = chr(64+int(min(max((x-60)*8/680+1,1),8)))
        lig = chr(57-int(min(max((y-60)*8/680+1,1),8)))
        return col, lig

    def coups_jouables(self,indice_piece:int ):
        """Retourne les coups jouables de la pièce indice_piece

        Args:
            echiquier (Echiquier): [description]
            piece (int): indice de la piece à analyser dans l'échiquier
        """
        liste_coups=[]
        p=self.echiquier[indice_piece]
        
        # ROI ------------------------------------------------------------------------------------------------
        if p.valeur=='Roi':
            for delta_col in (-1,0,1):
                for delta_lig in (-1,0,1):
                    new_coup=newCase(p.case,delta_col,delta_lig)
                    if new_coup!='' and new_coup not in liste_coups :
                        liste_coups.append(new_coup)
            if (self.case_précédente=='') and ((self.couleur=='blanc' and self.case=='E1') or (self.couleur=='noir' and self.case=='E8')):
                # condition nécessaire mais pas suffisante pour proposer un roque
                new_coup=newCase(self.case,2,0)
                liste_coups.append(new_coup)
                new_coup=newCase(self.case,-2,0)
                liste_coups.append(new_coup)
        # DAME ------------------------------------------------------------------------------------------------        
        if p.valeur=='Dame':
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
        if p.valeur=='Tour':
            for delta in range(-8,8):
                new_coup=newCase(self.case,delta,0)
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)        
                new_coup=newCase(self.case,0,delta)
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)
        # FOU ------------------------------------------------------------------------------------------------        
        if p.valeur=='Fou':
            for delta in range(-8,8):
                new_coup=newCase(self.case,delta,delta)
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)
                new_coup=newCase(self.case,delta,-delta)
                if new_coup!='' and new_coup not in liste_coups:
                    liste_coups.append(new_coup)
        # CAVALIER ------------------------------------------------------------------------------------------------        
        if p.valeur=='Cavalier':
            for delta_lig in (-2,2):
                for delta_col in (-1,1):
                    new_coup=newCase(self.case,delta_col,delta_lig)
                    if new_coup!='' and new_coup not in liste_coups:
                        liste_coups.append(new_coup)
                    new_coup=newCase(self.case,delta_lig,delta_col)
                    if new_coup!='' and new_coup not in liste_coups:
                        liste_coups.append(new_coup)
            # PION ------------------------------------------------------------------------------------------------        
        if p.valeur=='Pion':
            if p.couleur=='blanc':
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
        