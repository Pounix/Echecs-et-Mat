# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from src.class_echiquier import Commune
import unittest

class TestEchiquier(unittest.TestCase):
    def setUp(self):
        self.e=Echiquier()
        
    def test_xxxx(self):
        self.assertIsInstance(self.c,Echiquier)

        
if __name__== '__main__':
    unittest.main()