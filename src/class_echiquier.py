# -*- coding: utf-8 -*-
from sys import _current_frames
from PIL import Image
from class_piece import Piece
from moves import newCase


class Echiquier:
    def __init__(self,pieces={}):
        """Un Echiquier est dictionnaire de cases vides ou contenant une pièces

        Args:
            pieces {case:Piece} : dictionnaire de Piece avec la case ( ex. 'E4' ) pour clef
            si pieces est vide ==> nouvelle partie
        """
        self.pieces=pieces
        if self.pieces =={}:
            self.pieces = self.new_game()

    def new_game(self):
        """Creates a new game
        """
        self.pieces ={}
        lig = self._position_initiale(couleur='blanc',ligne='1')
        lig = self._position_initiale(couleur='noir',ligne='8')
        return self.pieces

    # To save typing parts for new_game twice
    def _position_initiale(self, couleur,ligne):
        # maintenant on place les pieces principales
        posinit=[('Roi','E'),('Dame','D'),('Fou','C'),('Cavalier','B'),('Tour','A'),('Fou','F'),('Cavalier','G'),('Tour','H')]
        for p in posinit:
            self.pieces[p[1]+ligne]=Piece(couleur=couleur,valeur=p[0],type=True,case_précédente=p[1]+ligne)

        # maintenant on place les pions
        # ligne = '2' if ligne=='1' else '7'
        # for c in "ABCDEFGH":
        #     self.pieces[c+ligne]=Piece(couleur=couleur,valeur='Pion',type=True,case_précédente=c+ligne)
        return

    def trace(self):
        """Trace le plateau de jeu

        Returns:
            image]: plateau avec ses pièces et ses éventuels curseurs
        """
        PLATEAU = Image.open("images\\échiquier.jpg")
        image_new = Image.new("RGB", (PLATEAU.width, PLATEAU.height))
        image_new.paste(PLATEAU, (0, 0))
        for p in self.pieces.keys():
            figurine = Image.open(self.pieces[p].fichier)
            c = int(198 + "ABCDEFGH".find(p[0]) * 288)
            l = int(2210 - "12345678".find(p[1]) * 288)
            image_new.paste(figurine, (c, l), figurine)

        # image_new.save('images\\mergedImages.png')
        return image_new

    def cleanCursor(self):
        """Ne conserve que les pièces de l'échiquier (retire les cursors)"""
        # l = {p.key: p.value for p in self.pieces if p.value.type}
        l = {p: self.pieces[p] for p in self.pieces if self.pieces[p].type}
        self.pieces = l
        return

    def ma_case(self, x, y):
        return ''.join(chr(64 + int(min(max((x - 60) * 8 / 680 + 1, 1), 8)))+chr(57 - int(min(max((y - 60) * 8 / 680 + 1, 1), 8))))

    def coups_jouables(self, case: str):
        """retourne un dictionnaire dont :
                la clef est chaque coup jouable
                la valeur chaque nouvelle liste de pièces correspondante, si ce coup était joué

        Args:
            case (str): case où se situe la pièce à analyser 
        """
        liste_coups = {}
        # pour éliminer une case ne contenant pas une pièce correcte
        try:
            if len(case)!=2:
                case='XX'
            val=self.pieces[case]
        except KeyError:
            return liste_coups
        
        valeur=self.pieces[case].valeur
        couleur=self.pieces[case].couleur
        # breakpoint()
        new_pieces={}
        # ROI ------------------------------------------------------------------------------------------------
        if valeur == "Roi":
            for delta_col in (-1, 0, 1):
                for delta_lig in (-1, 0, 1):
                    c=newCase(case,dir_nord=delta_lig,dir_ouest=delta_col)
                    if not c=='':
                        if c not in self.pieces.keys():
                            #la case est libre on peut jouer
                            new_ech=self.pieces.copy()
                            new_ech[c]=Piece(couleur=couleur,valeur=valeur,type=True,case_précédente=case)
                            del new_ech[case]
                            new_pieces[c]=new_ech
                        elif  couleur!=self.pieces[c].couleur:
                            #on peut prendre une pièce adverse
                            # breakpoint()
                            new_ech=self.pieces                            
                            new_ech[c]=Piece(couleur=couleur,valeur=valeur,type=True,case_précédente=case)
                            del new_ech[case]
                            new_pieces[c]=new_ech
        return new_pieces
    #                 new_coup = newCase(p.case, delta_col, delta_lig)
    #                 if new_coup != "" and new_coup not in liste_coups:
    #                     liste_coups.append(new_coup)
    #         if (self.case_précédente == "") and (
    #             (self.couleur == "blanc" and self.case == "E1")
    #             or (self.couleur == "noir" and self.case == "E8")
    #         ):
    #             # condition nécessaire mais pas suffisante pour proposer un roque
    #             new_coup = newCase(self.case, 2, 0)
    #             liste_coups.append(new_coup)
    #             new_coup = newCase(self.case, -2, 0)
    #             liste_coups.append(new_coup)
    #     # DAME ------------------------------------------------------------------------------------------------
    #     if p.valeur == "Dame":
    #         for delta in range(-8, 8):
    #             new_coup = newCase(self.case, delta, 0)
    #             if new_coup != "" and new_coup not in liste_coups:
    #                 liste_coups.append(new_coup)
    #             new_coup = newCase(self.case, 0, delta)
    #             if new_coup != "" and new_coup not in liste_coups:
    #                 liste_coups.append(new_coup)
    #             new_coup = newCase(self.case, delta, delta)
    #             if new_coup != "" and new_coup not in liste_coups:
    #                 liste_coups.append(new_coup)
    #             new_coup = newCase(self.case, delta, -delta)
    #             if new_coup != "" and new_coup not in liste_coups:
    #                 liste_coups.append(new_coup)
    #         # TOUR ------------------------------------------------------------------------------------------------
    #     if p.valeur == "Tour":
    #         for delta in range(-8, 8):
    #             new_coup = newCase(self.case, delta, 0)
    #             if new_coup != "" and new_coup not in liste_coups:
    #                 liste_coups.append(new_coup)
    #             new_coup = newCase(self.case, 0, delta)
    #             if new_coup != "" and new_coup not in liste_coups:
    #                 liste_coups.append(new_coup)
    #     # FOU ------------------------------------------------------------------------------------------------
    #     if p.valeur == "Fou":
    #         for delta in range(-8, 8):
    #             new_coup = newCase(self.case, delta, delta)
    #             if new_coup != "" and new_coup not in liste_coups:
    #                 liste_coups.append(new_coup)
    #             new_coup = newCase(self.case, delta, -delta)
    #             if new_coup != "" and new_coup not in liste_coups:
    #                 liste_coups.append(new_coup)
    #     # CAVALIER ------------------------------------------------------------------------------------------------
    #     if p.valeur == "Cavalier":
    #         for delta_lig in (-2, 2):
    #             for delta_col in (-1, 1):
    #                 new_coup = newCase(self.case, delta_col, delta_lig)
    #                 if new_coup != "" and new_coup not in liste_coups:
    #                     liste_coups.append(new_coup)
    #                 new_coup = newCase(self.case, delta_lig, delta_col)
    #                 if new_coup != "" and new_coup not in liste_coups:
    #                     liste_coups.append(new_coup)
    #         # PION ------------------------------------------------------------------------------------------------
    #     if p.valeur == "Pion":
    #         if p.couleur == "blanc":
    #             new_coup = newCase(self.case, 0, 1)
    #             if new_coup != "" and new_coup not in liste_coups:
    #                 liste_coups.append(new_coup)
    #             new_coup = newCase(self.case, 1, 1)  # Prise Piece
    #             if new_coup != "" and new_coup not in liste_coups:
    #                 liste_coups.append(new_coup)
    #             new_coup = newCase(self.case, -1, 1)  # Prise Piece
    #             if new_coup != "" and new_coup not in liste_coups:
    #                 liste_coups.append(new_coup)
    #             if self.ligne == "2":
    #                 new_coup = newCase(self.case, 0, 2)
    #                 if new_coup != "" and new_coup not in liste_coups:
    #                     liste_coups.append(new_coup)
    #         else:
    #             new_coup = newCase(self.case, 0, -1)
    #             if new_coup != "" and new_coup not in liste_coups:
    #                 liste_coups.append(new_coup)
    #             new_coup = newCase(self.case, 1, -1)  # Prise Piece
    #             if new_coup != "" and new_coup not in liste_coups:
    #                 liste_coups.append(new_coup)
    #             new_coup = newCase(self.case, -1, -1)  # Prise Piece
    #             if new_coup != "" and new_coup not in liste_coups:
    #                 liste_coups.append(new_coup)
    #             if self.ligne == "7":
    #                 new_coup = newCase(self.case, 0, -2)
    #                 if new_coup != "" and new_coup not in liste_coups:
    #                     liste_coups.append(new_coup)
