# -*- coding: utf-8 -*-

def newCase(case:str,dir_nord:int,dir_ouest:int):
    """ retourne la case = case+direction 
    case sous forme dir_nord:int,dir_ouest:int positif ou negatif
    retourne une case 'A5' ou '' si hors de l'échiquier 
    """
    case+="ZZ"  # au cas où case feariat moins de 2 caractères...
    col=ord(case[0])+dir_ouest
    lig=ord(case[1])+dir_nord
    if col<65 or col>72 or lig<49 or lig>56 or (dir_nord==0 and dir_ouest==0):
        return ''
    else:
        return chr(col)+chr(lig)