# -*- coding: utf-8 -*-

import sys
sys.path.append("F:\\OneDrive\\Coding\\Python\\Python3\\EchecEtMat")

from src.class_piece import Piece
import unittest

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.roi_1=Piece(valeur='Roi',couleur='blanc',colonne='E',ligne='1',déjà_bougé=False)
        self.roi_2=Piece(valeur='Roi',couleur='noir',colonne='E',ligne='8',déjà_bougé=False)
        self.roi_3=Piece(valeur='Roi',couleur='blanc',colonne='E',ligne='1',déjà_bougé=True)
        self.roi_4=Piece(valeur='Roi',couleur='noir',colonne='E',ligne='8',déjà_bougé=True)        
        self.roi_5=Piece(valeur='Roi',couleur='blanc',colonne='D',ligne='4',déjà_bougé=True)

        self.dame_1=Piece(valeur='Dame',couleur='blanc',colonne='D',ligne='4',déjà_bougé=False)
        self.tour_1=Piece(valeur='Tour',couleur='blanc',colonne='D',ligne='4',déjà_bougé=False)
        self.fou_1=Piece(valeur='Fou',couleur='blanc',colonne='D',ligne='4',déjà_bougé=False)
        self.cavalier_1=Piece(valeur='Cavalier',couleur='blanc',colonne='D',ligne='4',déjà_bougé=False)
        
        self.pion_1=Piece(valeur='Pion',couleur='blanc',colonne='D',ligne='4',déjà_bougé=False)
        self.pion_2=Piece(valeur='Pion',couleur='blanc',colonne='E',ligne='2',déjà_bougé=False)
        self.pion_3=Piece(valeur='Pion',couleur='noir',colonne='C',ligne='7',déjà_bougé=False)
        
    def test_mvt_roi(self):
        # test es possibilités de Roque
        self.assertIn('C1',self.roi_1.coups_possibles)
        self.assertIn('C8',self.roi_2.coups_possibles)
        self.assertNotIn('C1',self.roi_3.coups_possibles)
        self.assertNotIn('C8',self.roi_4.coups_possibles)
        
        self.assertIn('G1',self.roi_1.coups_possibles)
        self.assertIn('G8',self.roi_2.coups_possibles)
        self.assertNotIn('G1',self.roi_3.coups_possibles)
        self.assertNotIn('G8',self.roi_4.coups_possibles)
                
        self.assertIn('C3',self.roi_5.coups_possibles)
        self.assertIn('E5',self.roi_5.coups_possibles)
        self.assertIn('D5',self.roi_5.coups_possibles)
        self.assertNotIn('C1',self.roi_5.coups_possibles)

    def test_mvt_dame(self):
        # test es possibilités de Roque
        self.assertIn('F6',self.dame_1.coups_possibles)
        self.assertIn('C3',self.dame_1.coups_possibles)
        self.assertIn('H8',self.dame_1.coups_possibles)
        self.assertNotIn('F1',self.dame_1.coups_possibles)
        
    def test_mvt_tour(self):
        self.assertIn('D2',self.tour_1.coups_possibles)
        self.assertIn('D8',self.tour_1.coups_possibles)
        self.assertIn('A4',self.tour_1.coups_possibles)
        self.assertNotIn('C3',self.tour_1.coups_possibles)
    
    def test_mvt_fou(self):
        self.assertIn('E5',self.fou_1.coups_possibles)
        self.assertIn('B2',self.fou_1.coups_possibles)
        self.assertIn('F2',self.fou_1.coups_possibles)
        self.assertNotIn('F1',self.fou_1.coups_possibles)
    
    def test_mvt_cavalier(self):
        self.assertIn('E6',self.cavalier_1.coups_possibles)
        self.assertIn('C6',self.cavalier_1.coups_possibles)
        self.assertIn('B3',self.cavalier_1.coups_possibles)
        self.assertNotIn('D3',self.cavalier_1.coups_possibles)
        
    def test_mvt_pion(self):
        self.assertIn('D5',self.pion_1.coups_possibles)
        self.assertNotIn('D6',self.pion_1.coups_possibles)
        self.assertNotIn('C5',self.pion_1.coups_possibles)
        
        self.assertIn('E3',self.pion_2.coups_possibles)
        self.assertIn('E4',self.pion_2.coups_possibles)
        self.assertNotIn('E5',self.pion_2.coups_possibles)
        
        self.assertIn('C6',self.pion_3.coups_possibles)
        self.assertIn('C5',self.pion_3.coups_possibles)
        self.assertNotIn('C8',self.pion_3.coups_possibles)
        
        
if __name__== '__main__':
    unittest.main()