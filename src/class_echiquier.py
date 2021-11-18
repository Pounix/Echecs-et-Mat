# -*- coding: utf-8 -*-
from sys import _current_frames
from PIL import Image
from class_piece import Piece
from moves import newCase


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
        lig = self._position_initiale(couleur='blanc',ligne='1')
        lig = self._position_initiale(couleur='noir',ligne='8')
        return self.pieces

    def _position_initiale(self, couleur,ligne):
        # maintenant on place les pieces principales
        posinit=[('Roi','E'),('Dame','D'),('Fou','C'),('Cavalier','B'),('Tour','A'),('Fou','F'),('Cavalier','G'),('Tour','H')]
        for p in posinit:
            self.pieces[p[1]+ligne]=Piece(couleur=couleur,valeur=p[0],type=True,case_précédente=p[1]+ligne)

        # # maintenant on place les pions
        # ligne = '2' if ligne=='1' else '7'
        # for c in "ABCDEFGH":
        #     self.pieces[c+ligne]=Piece(couleur=couleur,valeur='Pion',type=True,case_précédente=c+ligne)
        # return

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


        