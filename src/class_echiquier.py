# -*- coding: utf-8 -*-
from sys import _current_frames
from PIL import Image
from class_piece import Piece
from moves import newCase, attaquable_par
from settings import COULEUR, VALEUR, PLATEAU_JPG

class Echiquier:
    def __init__(self,pieces={}):
        """Un Echiquier est dictionnaire de cases contenant chacune une pièces et/ou un cursor
            si l'argument piece ={} ==> on initialise une nouvelle partie
        Args:
            pieces {case:Piece} : pieces.key='E4' .value=Piece 
        """
        self.pieces=pieces
        if self.pieces =={}:
            self.pieces = self.new_game()

    def new_game(self):
        """Creates a new game
        """
        self.pieces ={}
        self._position_initiale(couleur=0,ligne='1')
        self._position_initiale(couleur=1,ligne='8')
        return self.pieces

    def _position_initiale(self, couleur,ligne):
        # maintenant on place les pieces principales
        posinit=[(0,'E'),(1,'D'),(2,'C'),(3,'B'),(4,'A'),(2,'F'),(3,'G'),(4,'H')]
        for p in posinit:
            self.pieces[p[1]+ligne]=Piece(couleur=couleur,valeur=p[0],case_précédente=p[1]+ligne,case_coup_précédent=p[1]+ligne)

        # maintenant on place les pions
        ligne = '2' if ligne=='1' else '7'
        for c in "ABCDEFGH":
            self.pieces[c+ligne]=Piece(couleur=couleur,valeur=5,case_précédente=c+ligne,case_coup_précédent=c+ligne)
        return

    def trace(self):
        """Trace le plateau de jeu

        Returns:
            image: plateau avec ses pièces et ses éventuels curseurs
        """
        PLATEAU=Image.open(PLATEAU_JPG)
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
        l = {p: self.pieces[p] for p in self.pieces if self.pieces[p].valeur<6}
        self.pieces = l
        return

    def ma_case(self, x, y):
        return ''.join(chr(64 + int(min(max((x - 60) * 8 / 680 + 1, 1), 8)))+chr(57 - int(min(max((y - 60) * 8 / 680 + 1, 1), 8))))


    def check_échec(self):
        """ ajoute les marques de mies en échec ( Cursor_échec) éventuelles
        """
        for p in self.pieces.keys():
            if self.pieces[p].valeur==0 and attaquable_par(self.pieces,p,1-self.pieces[p].couleur): # c'est un Roi, est-il en échec
                return p
        return ''