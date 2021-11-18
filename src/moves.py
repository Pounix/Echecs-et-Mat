# -*- coding: utf-8 -*-

from tkinter.constants import FALSE


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
    
def coups_jouables(pieces, case_départ: str):
    """retourne les coups jouables par la pièce située en case_départ 

    Args:
        pieces(dict) : dictionnaire de pieces
        case_départ (str): du genre 'F3'

    Returns:
        liste_coups {case,pieces} : donc c'est un dictionnaire de dictionnaires...
    """
    liste_coups = {}
    try:  # pour éliminer une case ne contenant pas une pièce correcte
        if len(case_départ)!=2:
            case='XX'
        valeur=pieces[case_départ].valeur
    except KeyError:
        return liste_coups

    if valeur=='Roi':
        liste_coups = mouvements_possibles_roi(pieces,case_départ)
    elif valeur=='Dame':
        liste_coups = mouvements_possibles_dame(pieces,case_départ)    
    elif valeur=='Tour':
        liste_coups = mouvements_possibles_tour(pieces,case_départ) 
    elif valeur=='Fou':
        liste_coups = mouvements_possibles_fou(pieces,case_départ) 
    elif valeur=='Cavalier':
        liste_coups = mouvements_possibles_cavalier(pieces,case_départ) 
    elif valeur=='Pion':
        liste_coups = mouvements_possibles_pion(pieces,case_départ)
        
    # TODO possibilité de 'prise en passant' d'un pion
               
    return liste_coups 

def mouvements_possibles_roi(pieces, case_départ: str):
    """ ROI : Liste des coups jouables du Roi situé en 'case_départ'

    Args:
        case_départ(str): case à analyser sous forme 'B2'

    Returns:
        coups_possibles {case,pieces} : donc c'est un dictionnaire de dictionnaires...
    """
    coups_possibles={}
    for delta_col in (-1, 0, 1):
        for delta_lig in (-1, 0, 1):
            case_arrivée=newCase(case=case_départ,dir_nord=delta_lig,dir_ouest=delta_col)
            if case_arrivée != '' and (
                case_arrivée not in pieces.keys()
                or case_arrivée in pieces.keys()
                and pieces[case_départ].couleur != pieces[case_arrivée].couleur
            ):
                #la case est libre on peut jouer
                coups_possibles[case_arrivée]= déplace_une_piece(pieces, case_départ=case_départ,case_arrivée=case_arrivée)
    flg=False
    if pieces[case_départ].case_précédente==case_départ:   # c'est bon le roi n'a jamais bougé !            
        # test petit ROQUE
        color = 'noir' if pieces[case_départ].couleur=='blanc' else 'blanc'
        delta_lig=0
        pos_tour = 'H1' if pieces[case_départ].couleur=='blanc' else 'H8'
        if pos_tour in pieces.keys() and pieces[pos_tour].case_précédente==pos_tour:   # Il y a une tour et elle n'a pas bougé non plus !
            flg=True
            for delta_col in (1,2):
                case_arrivée=newCase(case=case_départ,dir_nord=delta_lig,dir_ouest=delta_col)
                if case_arrivée in pieces.keys():
                    flg=False
                    break
                elif attaquable_par(pieces=pieces,case=case_arrivée,couleur_attaquant=color):
                    flg=False
                    break
            if flg:
                new_pos_roi=newCase(case=case_départ,dir_nord=delta_lig,dir_ouest=2)
                new_pos_tour=newCase(case=case_départ,dir_nord=delta_lig,dir_ouest=1)
                cp=déplace_une_piece(pieces, case_départ=pos_tour,case_arrivée=new_pos_tour)
                coups_possibles[new_pos_roi]=déplace_une_piece(cp, case_départ=case_départ,case_arrivée=new_pos_roi)
        # test grand ROQUE
        pos_tour = 'A1' if pieces[case_départ].couleur=='blanc' else 'A8'
        if pos_tour in pieces.keys() and pieces[pos_tour].case_précédente==pos_tour:   # Il y a une tour et elle n'a pas bougé non plus !
            flg=True
            for delta_col in (1,3):
                case_arrivée=newCase(case=case_départ,dir_nord=delta_lig,dir_ouest=-delta_col)
                if case_arrivée in pieces.keys():
                    flg=False
                    break
                elif attaquable_par(pieces=pieces,case=case_arrivée,couleur_attaquant=color):
                    flg=False
                    break
            if flg:
                new_pos_roi=newCase(case=case_départ,dir_nord=delta_lig,dir_ouest=-2)
                new_pos_tour=newCase(case=case_départ,dir_nord=delta_lig,dir_ouest=-1)
                cp=déplace_une_piece(pieces, case_départ=pos_tour,case_arrivée=new_pos_tour)
                coups_possibles[new_pos_roi]=déplace_une_piece(cp, case_départ=case_départ,case_arrivée=new_pos_roi)
                
    return coups_possibles

def mouvements_possibles_cavalier(pieces, case_départ: str):
    """ CAVALIER : Liste des coups jouables du Cavalier situé en 'case_départ'

    Args:
        case_départ(str): case à analyser sous forme 'B2'

    Returns:
        Liste de cases jouables : ['B2', 'B3',...]
    """
    coups_possibles={}
    for delta_lig in (-2, 2):
        for delta_col in (-1, 1):
            case_arrivée=newCase(case=case_départ,dir_nord=delta_lig,dir_ouest=delta_col)
            if case_arrivée != '' and (
                case_arrivée not in pieces.keys()
                or case_arrivée in pieces.keys()
                and pieces[case_départ].couleur != pieces[case_arrivée].couleur
            ):
                #la case est libre on peut jouer
                coups_possibles[case_arrivée]= déplace_une_piece(pieces, case_départ=case_départ,case_arrivée=case_arrivée)  
    for delta_lig in (-1, 1):
        for delta_col in (-2, 2):
            case_arrivée=newCase(case=case_départ,dir_nord=delta_lig,dir_ouest=delta_col)
            if case_arrivée != '' and (
                case_arrivée not in pieces.keys()
                or case_arrivée in pieces.keys()
                and pieces[case_départ].couleur != pieces[case_arrivée].couleur
            ):
                #la case est libre on peut jouer
                coups_possibles[case_arrivée]= déplace_une_piece(pieces, case_départ=case_départ,case_arrivée=case_arrivée)  
    return coups_possibles
                
def mouvements_possibles_dame(pieces, case_départ: str):
    """ DAME : Liste des coups jouables de la Dame située en 'case_départ'

    Args:
        case_départ(str): case à analyser sous forme 'B2'

    Returns:
        coups_possibles {case,pieces} : donc c'est un dictionnaire de dictionnaires...
    """
    coups_possibles=mouvements_possibles_tour(pieces=pieces,case_départ=case_départ)
    coups_possibles.update(mouvements_possibles_fou(pieces,case_départ))
    return coups_possibles
                    
def mouvements_possibles_tour(pieces, case_départ: str):
    """ TOUR : Liste des coups jouables de la Tour située en 'case_départ'

    Args:
        case_départ(str): case à analyser sous forme 'B2'

    Returns:
        Liste de cases jouables : ['B2', 'B3',...]
    """
    coups_possibles={}
    delta_lig=0
    for delta_col in (-1, 1):
        for i in range(1,8):
            case_arrivée=newCase(case=case_départ,dir_nord=delta_lig*i,dir_ouest=delta_col*i)
            if case_arrivée != '' and case_arrivée not in pieces.keys():
                #la case est libre on peut jouer
                coups_possibles[case_arrivée]= déplace_une_piece(pieces, case_départ=case_départ,case_arrivée=case_arrivée)  
            elif (
                case_arrivée != ''
                and case_arrivée in pieces.keys()
                and pieces[case_départ].couleur != pieces[case_arrivée].couleur
            ):
                #on peut prendre une pièce adverse
                # breakpoint()
                coups_possibles[case_arrivée]= déplace_une_piece(pieces, case_départ=case_départ,case_arrivée=case_arrivée)  
                break
            else:
                break
    delta_col=0
    for delta_lig in (-1, 1):
        for i in range(1,8):
            case_arrivée=newCase(case=case_départ,dir_nord=delta_lig*i,dir_ouest=delta_col*i)
            if case_arrivée != '' and case_arrivée not in pieces.keys():
                #la case est libre on peut jouer
                coups_possibles[case_arrivée]= déplace_une_piece(pieces, case_départ=case_départ,case_arrivée=case_arrivée)  
            elif (
                case_arrivée != ''
                and case_arrivée in pieces.keys()
                and pieces[case_départ].couleur != pieces[case_arrivée].couleur
            ):
                #on peut prendre une pièce adverse
                # breakpoint()
                coups_possibles[case_arrivée]= déplace_une_piece(pieces, case_départ=case_départ,case_arrivée=case_arrivée)  
                break
            else:
                break
    return coups_possibles

def mouvements_possibles_fou(pieces, case_départ: str):
    """ FOU : Liste des coups jouables du Fou situé en 'case_départ'

    Args:
        case_départ(str): case à analyser sous forme 'B2'

    Returns:
        coups_possibles {case,pieces} : donc c'est un dictionnaire de dictionnaires...
    """
    coups_possibles={}
    for delta_col in (-1, 1):
        delta_lig=delta_col
        for i in range(1,8):
            case_arrivée=newCase(case=case_départ,dir_nord=delta_lig*i,dir_ouest=delta_col*i)
            if case_arrivée != '' and case_arrivée not in pieces.keys():
                #la case est libre on peut jouer
                coups_possibles[case_arrivée]= déplace_une_piece(pieces, case_départ=case_départ,case_arrivée=case_arrivée)  
            elif (
                case_arrivée != ''
                and case_arrivée in pieces.keys()
                and pieces[case_départ].couleur != pieces[case_arrivée].couleur
            ):
                #on peut prendre une pièce adverse
                # breakpoint()
                coups_possibles[case_arrivée]= déplace_une_piece(pieces, case_départ=case_départ,case_arrivée=case_arrivée)  
                break
            else:
                break
    for delta_col in (-1, 1):
        delta_lig=-delta_col
        for i in range(1,8):
            case_arrivée=newCase(case=case_départ,dir_nord=delta_lig*i,dir_ouest=delta_col*i)
            if case_arrivée != '' and case_arrivée not in pieces.keys():
                #la case est libre on peut jouer
                coups_possibles[case_arrivée]= déplace_une_piece(pieces, case_départ=case_départ,case_arrivée=case_arrivée)  
            elif (
                case_arrivée != ''
                and case_arrivée in pieces.keys()
                and pieces[case_départ].couleur != pieces[case_arrivée].couleur
            ):
                #on peut prendre une pièce adverse
                # breakpoint()
                coups_possibles[case_arrivée]= déplace_une_piece(pieces, case_départ=case_départ,case_arrivée=case_arrivée)  
                break
            else:
                break
    return coups_possibles

def mouvements_possibles_pion(pieces, case_départ: str):
    """ PION : Liste des coups jouables du Pion situé en 'case_départ'

    Args:
        case_départ(str): case à analyser sous forme 'B2'

    Returns:
        coups_possibles {case,pieces} : donc c'est un dictionnaire de dictionnaires...
    """
    coups_possibles={}
    # mouvement pion classique de 1 selon couleur du pion
    delta_lig =1 if pieces[case_départ].couleur=='blanc'else -1
    delta_col=0
    case_arrivée=newCase(case=case_départ,dir_nord=delta_lig,dir_ouest=delta_col)
    if case_arrivée not in pieces.keys():
        #la case est libre on peut jouer
        coups_possibles[case_arrivée]= déplace_une_piece(pieces, case_départ,case_arrivée,) 

        # mouvement pion 2 cases à l'ouverture uniquement
        if case_départ==pieces[case_départ].case_précédente:   # donc si le pion n'a pas encore bougé
            delta_lig =2 if pieces[case_départ].couleur=='blanc'else -2
            delta_col=0
            case_arrivée=newCase(case_départ,dir_nord=delta_lig,dir_ouest=delta_col)
            if case_arrivée not in pieces.keys():
                #la case est libre on peut jouer
                coups_possibles[case_arrivée]= déplace_une_piece(pieces, case_départ=case_départ,case_arrivée=case_arrivée)  

    # mouvement pion pour la prise d'une pièce
    delta_lig =1 if pieces[case_départ].couleur=='blanc'else -1
    for delta_col in (-1,1):
        case_arrivée=newCase(case=case_départ,dir_nord=delta_lig,dir_ouest=delta_col)
        if (
            case_arrivée in pieces.keys()
            and pieces[case_arrivée].couleur != pieces[case_départ].couleur
        ):
            # on peut prendre une pièce adverse
            coups_possibles[case_arrivée]= déplace_une_piece(pieces, case_départ=case_départ,case_arrivée=case_arrivée)  
    return coups_possibles        

def déplace_une_piece(pieces, case_départ: str, case_arrivée: str):
    """MOUVEMENT D'UNE PIECE : retourne une liste de pièces après le mouvement d'une pièce

    Args:
        case_départ (str)  : la case de la pièce à déplacer
        case_arrivée (str) : la case de destination

    Returns:
        new_pieces (dict): le dictionnaire des pièces après ce coup
    """
    
    new_pieces=pieces.copy()                            
    new_pieces[case_arrivée]=pieces[case_départ]
    new_pieces[case_arrivée].case_précédente=case_départ
    del new_pieces[case_départ]
    return new_pieces

def attaquable_par(pieces,case,couleur_attaquant):
    """vérifie si case est attaquable par une des pieces de couleur

    Args:
        pieces (dict): dictionnaire {case, piece}
        case (str): case du genre 'A2'
        couleur (str): 'blanc' ou 'noir'

    Returns:
        bool : True = case est attaquable par couleur   False = il ne l'est pas, pardi !
    """
    print('Analyse attaque', case,'par', couleur_attaquant,': Jeu =', pieces.keys())
    attaque=False
    for key in pieces:
        piece=pieces[key]
        if piece.couleur==couleur_attaquant:
            cj=coups_jouables(pieces=pieces, case_départ=key)
            print ('> coups jouables par',piece,cj.keys())
            if case in cj:
                attaque=True
                break
    return attaque  


    # return any(
    #     p.type
    #     and p.couleur == couleur_attaquant
    #     and case in coups_jouables(pieces=pieces, case_départ=case)
    #     for p in pieces.values()
    # )
    
def elimine_coups_provoquant_echec(liste_coups, couleur_attaquant):
    """Elimine les coups possibles provoquant une mise en échec par les 'couleur'

    Args:
        liste_coups {case,pieces} : donc c'est un dictionnaire de dictionnaires...
        couleur (str): couleur de l'attaquant

    Returns:
        liste_coups {case,pieces} : donc c'est un dictionnaire de dictionnaires...
    """
    
    # trouver le Roi de même couleur que la pièce de case_départ
    position_du_roi='?'
    lc=liste_coups.copy()
    flg=False
    for key in lc:
        pieces=lc[key]
        for key2 in pieces:
            piece=pieces[key2]
            if piece.couleur!=couleur_attaquant and piece.valeur=='Roi':
                position_du_roi=key2
                flg=True        # on a trouvé le Roi !!!
                break
        if flg and attaquable_par(pieces=pieces,case=position_du_roi,couleur_attaquant=couleur_attaquant):
                del liste_coups[key]
    return liste_coups
