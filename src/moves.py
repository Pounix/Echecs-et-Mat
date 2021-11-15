# -*- coding: utf-8 -*-
from class_echiquier import Echiquier
import class_piece


def newCase(case,delta_col,delta_lig):
    """retourne la case case+delta_lig+delta_col ou '' si hors de l'échiquier

    Args:
        case ([type]): [description]
        delta_lig ([type]): [description]
        delat_col ([type]): [description]
    """
    col=ord(case[0])+delta_col
    lig=ord(case[1])+delta_lig
    
    if col>64 and col<73 and lig>48 and lig<57 and not (delta_col==0 and delta_lig==0):
        return ''.join(chr(col)+chr(lig))
    else:
         return ''

