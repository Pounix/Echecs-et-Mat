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

    # To save typing parts for new_game twice
    def _position_initiale(self, couleur,ligne):
        # maintenant on place les pieces principales
        posinit=[('Roi','E'),('Dame','D'),('Fou','C'),('Cavalier','B'),('Tour','A'),('Fou','F'),('Cavalier','G'),('Tour','H')]
        for p in posinit:
            self.pieces[p[1]+ligne]=Piece(couleur=couleur,valeur=p[0],type=True,case_précédente=p[1]+ligne)

        # maintenant on place les pions
        ligne = '2' if ligne=='1' else '7'
        for c in "ABCDEFGH":
            self.pieces[c+ligne]=Piece(couleur=couleur,valeur='Pion',type=True,case_précédente=c+ligne)
        return

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

    def coups_jouables(self, case_départ: str):
        """retourne les coups jouables par la pièce située en case_départ 

        Args:
            case_départ (str): du genre 'F3'

        Returns:
            coups_possibles {case,pieces} : donc c'est un dictionnaire de dictionnaires...
        """
        liste_coups = {}
        
        try:  # pour éliminer une case ne contenant pas une pièce correcte
            if len(case_départ)!=2:
                case='XX'
            valeur=self.pieces[case_départ].valeur
        except KeyError:
            return liste_coups

        if valeur=='Roi':
            liste_coups = self.mouvements_possibles_roi(case_départ)
        elif valeur=='Dame':
            liste_coups = self.mouvements_possibles_dame(case_départ)    
        elif valeur=='Tour':
            liste_coups = self.mouvements_possibles_tour(case_départ) 
        elif valeur=='Fou':
            liste_coups = self.mouvements_possibles_fou(case_départ) 
        elif valeur=='Cavalier':
            liste_coups = self.mouvements_possibles_cavalier(case_départ) 
        elif valeur=='Pion':
            liste_coups = self.mouvements_possibles_pion(case_départ)
            
        # TODO possibilité de 'prise en passant' d'un pion
        return liste_coups 

    def mouvements_possibles_roi(self, case_départ: str):
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
                    case_arrivée not in self.pieces.keys()
                    or case_arrivée in self.pieces.keys()
                    and self.pieces[case_départ].couleur != self.pieces[case_arrivée].couleur
                ):
                    #la case est libre on peut jouer
                    coups_possibles[case_arrivée]= self.déplace_une_piece(case_départ=case_départ,case_arrivée=case_arrivée)  
        #TODO cas des roques
        return coups_possibles
    
    def mouvements_possibles_cavalier(self, case_départ: str):
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
                    case_arrivée not in self.pieces.keys()
                    or case_arrivée in self.pieces.keys()
                    and self.pieces[case_départ].couleur != self.pieces[case_arrivée].couleur
                ):
                    #la case est libre on peut jouer
                    coups_possibles[case_arrivée]= self.déplace_une_piece(case_départ=case_départ,case_arrivée=case_arrivée)  
        for delta_lig in (-1, 1):
            for delta_col in (-2, 2):
                case_arrivée=newCase(case=case_départ,dir_nord=delta_lig,dir_ouest=delta_col)
                if case_arrivée != '' and (
                    case_arrivée not in self.pieces.keys()
                    or case_arrivée in self.pieces.keys()
                    and self.pieces[case_départ].couleur != self.pieces[case_arrivée].couleur
                ):
                    #la case est libre on peut jouer
                    coups_possibles[case_arrivée]= self.déplace_une_piece(case_départ=case_départ,case_arrivée=case_arrivée)  
        return coups_possibles
                    
    def mouvements_possibles_dame(self, case_départ: str):
        """ DAME : Liste des coups jouables de la Dame située en 'case_départ'

        Args:
            case_départ(str): case à analyser sous forme 'B2'

        Returns:
            coups_possibles {case,pieces} : donc c'est un dictionnaire de dictionnaires...
        """
        coups_possibles=self.mouvements_possibles_tour(case_départ)
        coups_possibles.update(self.mouvements_possibles_fou(case_départ))
        return coups_possibles
                        
    def mouvements_possibles_tour(self, case_départ: str):
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
                if case_arrivée != '' and case_arrivée not in self.pieces.keys():
                    #la case est libre on peut jouer
                    coups_possibles[case_arrivée]= self.déplace_une_piece(case_départ=case_départ,case_arrivée=case_arrivée)  
                elif (
                    case_arrivée != ''
                    and case_arrivée in self.pieces.keys()
                    and self.pieces[case_départ].couleur != self.pieces[case_arrivée].couleur
                ):
                    #on peut prendre une pièce adverse
                    # breakpoint()
                    coups_possibles[case_arrivée]= self.déplace_une_piece(case_départ=case_départ,case_arrivée=case_arrivée)  
                    break
                else:
                    break
        delta_col=0
        for delta_lig in (-1, 1):
            for i in range(1,8):
                case_arrivée=newCase(case=case_départ,dir_nord=delta_lig*i,dir_ouest=delta_col*i)
                if case_arrivée != '' and case_arrivée not in self.pieces.keys():
                    #la case est libre on peut jouer
                    coups_possibles[case_arrivée]= self.déplace_une_piece(case_départ=case_départ,case_arrivée=case_arrivée)  
                elif (
                    case_arrivée != ''
                    and case_arrivée in self.pieces.keys()
                    and self.pieces[case_départ].couleur != self.pieces[case_arrivée].couleur
                ):
                    #on peut prendre une pièce adverse
                    # breakpoint()
                    coups_possibles[case_arrivée]= self.déplace_une_piece(case_départ=case_départ,case_arrivée=case_arrivée)  
                    break
                else:
                    break
        return coups_possibles

    def mouvements_possibles_fou(self, case_départ: str):
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
                if case_arrivée != '' and case_arrivée not in self.pieces.keys():
                    #la case est libre on peut jouer
                    coups_possibles[case_arrivée]= self.déplace_une_piece(case_départ=case_départ,case_arrivée=case_arrivée)  
                elif (
                    case_arrivée != ''
                    and case_arrivée in self.pieces.keys()
                    and self.pieces[case_départ].couleur != self.pieces[case_arrivée].couleur
                ):
                    #on peut prendre une pièce adverse
                    # breakpoint()
                    coups_possibles[case_arrivée]= self.déplace_une_piece(case_départ=case_départ,case_arrivée=case_arrivée)  
                    break
                else:
                    break
        for delta_lig in (-1, 1):
            delta_col=-delta_lig
            for i in range(1,8):
                case_arrivée=newCase(case=case_départ,dir_nord=delta_lig*i,dir_ouest=delta_col*i)
                if case_arrivée != '' and case_arrivée not in self.pieces.keys():
                    #la case est libre on peut jouer
                    coups_possibles[case_arrivée]= self.déplace_une_piece(case_départ=case_départ,case_arrivée=case_arrivée)  
                elif (
                    case_arrivée != ''
                    and case_arrivée in self.pieces.keys()
                    and self.pieces[case_départ].couleur != self.pieces[case_arrivée].couleur
                ):
                    #on peut prendre une pièce adverse
                    # breakpoint()
                    coups_possibles[case_arrivée]= self.déplace_une_piece(case_départ=case_départ,case_arrivée=case_arrivée)  
                    break
                else:
                    break
        return coups_possibles

    def mouvements_possibles_pion(self, case_départ: str):
        """ PION : Liste des coups jouables du Pion situé en 'case_départ'

        Args:
            case_départ(str): case à analyser sous forme 'B2'

        Returns:
            coups_possibles {case,pieces} : donc c'est un dictionnaire de dictionnaires...
        """
        coups_possibles={}
        # mouvement pion classique de 1 selon couleur du pion
        delta_lig =1 if self.pieces[case_départ].couleur=='blanc'else -1
        delta_col=0
        case_arrivée=newCase(case=case_départ,dir_nord=delta_lig,dir_ouest=delta_col)
        if case_arrivée not in self.pieces.keys():
            #la case est libre on peut jouer
            coups_possibles[case_arrivée]= self.déplace_une_piece(case_départ,case_arrivée,) 

            # mouvement pion 2 cases à l'ouverture uniquement
            if case_départ==self.pieces[case_départ].case_précédente:   # donc si le pion n'a pas encore bougé
                delta_lig =2 if self.pieces[case_départ].couleur=='blanc'else -2
                delta_col=0
                case_arrivée=newCase(case_départ,dir_nord=delta_lig,dir_ouest=delta_col)
                if case_arrivée not in self.pieces.keys():
                    #la case est libre on peut jouer
                    coups_possibles[case_arrivée]= self.déplace_une_piece(case_départ=case_départ,case_arrivée=case_arrivée)  

        # mouvement pion pour la prise d'une pièce
        delta_lig =1 if self.pieces[case_départ].couleur=='blanc'else -1
        for delta_col in (-1,1):
            case_arrivée=newCase(case=case_départ,dir_nord=delta_lig,dir_ouest=delta_col)
            if (
                case_arrivée in self.pieces.keys()
                and self.pieces[case_arrivée].couleur != self.pieces[case_départ].couleur
            ):
                # on peut prendre une pièce adverse
                coups_possibles[case_arrivée]= self.déplace_une_piece(case_départ=case_départ,case_arrivée=case_arrivée)  
        return coups_possibles        
    
    def déplace_une_piece(self, case_départ: str, case_arrivée: str):
        """MOUVEMENT D'UNE PIECE : retourne une liste de pièces après le mouvement d'une pièce

        Args:
            case_départ (str)  : la case de la pièce à déplacer
            case_arrivée (str) : la case de destination

        Returns:
            new_pieces (dict): le dictionnaire des pièces après ce coup
        """
        print('case_départ = ',case_départ,'   / case_arrivée = ',case_arrivée)
        new_pieces=self.pieces.copy()                            
        new_pieces[case_arrivée]=self.pieces[case_départ]
        new_pieces[case_arrivée].case_précédente=case_départ
        del new_pieces[case_départ]
        return new_pieces