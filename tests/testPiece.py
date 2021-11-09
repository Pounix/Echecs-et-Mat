# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from src.class_Piece import Commune
import unittest

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.e=Piece()
        
    def test_xxxx(self):
        self.assertIsInstance(self.c,Piece)

        
if __name__== '__main__':
    unittest.main()