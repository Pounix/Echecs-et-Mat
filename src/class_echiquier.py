# -*- coding: utf-8 -*-
from PIL import Image
from src.class_piece import Piece

class Echiquier:
    
       
    def __init__(self):
        """Un Echiquier est une liste de Piece

        Args:
            echiquier ([type]): [description]
        """

        
    def new_game(self,couleur_joueur : str ='blanc'):
        """Creates a new game for player couleur_joueur

        Args:
            couleur_joueur = 'blanc' ou 'noir' à mettre en bas de l'echiquier
        """
        self.echiquier = []
        col=couleur_joueur
        lig = self._extracted_from_new_game('1', col, '2')
        col = 'noir' if col=='blanc' else 'blanc'
        lig = self._extracted_from_new_game('8', col, '7')
        return self.echiquier

    # To save typing parts for new_game twice
    def _extracted_from_new_game(self, arg0, col, ligne):
        result = arg0
        self.echiquier.append(Piece(col, valeur='Roi', ligne=result, colonne='E'))
        self.echiquier.append(Piece(col, valeur='Dame', ligne=result, colonne='D'))
        self.echiquier.append(Piece(col, valeur='Fou', ligne=result, colonne='C'))
        self.echiquier.append(Piece(col, valeur='Fou', ligne=result, colonne='F'))
        self.echiquier.append(Piece(col, valeur='Cavalier', ligne=result, colonne='B'))
        self.echiquier.append(Piece(col, valeur='Cavalier', ligne=result, colonne='G'))
        self.echiquier.append(Piece(col, valeur='Tour', ligne=result, colonne='A'))
        self.echiquier.append(Piece(col, valeur='Tour', ligne=result, colonne='H'))
        for c in 'ABCDEFGH':
            self.echiquier.append(Piece(col, valeur='Pion', ligne=ligne, colonne=c))

        return result

    def trace(self):
        PLATEAU = Image.open('images\\échiquier.jpg')
        image_new = Image.new('RGB',(PLATEAU.width,PLATEAU.height))
        image_new.paste(PLATEAU,(0,0))
        for p in self.echiquier:
            figurine = Image.open(p.fichier)
            c=int(198+'ABCDEFGH'.find(p.colonne)*288)
            l=int(190+'12345678'.find(p.ligne)*288)
            image_new.paste(figurine,(c,l),figurine)

        image_new.save('images\\mergedImages.png')
        return image_new