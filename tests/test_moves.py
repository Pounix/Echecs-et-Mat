# -*- coding: utf-8 -*-

import sys
sys.path.append("F:\\OneDrive\\Coding\\Python\\Python3\\EchecEtMat")

from src.moves import newCase
import unittest

class TestnewCase(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_que_ca_bouge(self):
        self.assertEqual(newCase('E2',0,0),'')      # because pas de mouvement ...
        self.assertEqual(newCase('A7',1,1),'B8')
        self.assertEqual(newCase('F1',1,5),'G6')
        self.assertEqual(newCase('B8',2,-3),'D5')
        self.assertEqual(newCase('G8',-2,-8),'')    #because hors de l'echiquier
        self.assertEqual(newCase('H6',0,-1),'H5')
        self.assertEqual(newCase('A1',3,2),'D3')
        self.assertEqual(newCase('F2',1,2),'G4')

        
if __name__== '__main__':
    unittest.main()