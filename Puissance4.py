def grille_vide() :
    ''' Construit un tableau à deux dimension 6 lignes et 7 colonnes où chaque case contient la valeur 0.
    La fonction renvoie le tableau.'''
    grille = []
    for i in range(6):
        grille.append([])
    for i in grille :
        for j in range(7) :
            i.append(0)
    return grille
assert grille_vide() == [[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]


def coup_possible(gril,col) :
    '''
    Détermine si possible de jouer dans la colone col
    Prend en argument la grille, tableau 7x6, avec la position des pions des joueurs et un entier, le numéro de colone entre 0 et 6.
    Renvoie True si possible de jouer dans la colone col, False sinon.
    '''
    if gril[0][col]==0 :
        return True
    else :
        return False
gril=[[2,0,0,0,0,0,0],
      [2,0,0,0,0,0,0],
      [2,0,0,0,0,0,0],
      [2,0,0,0,0,0,0],
      [2,0,0,0,0,0,0],
      [2,0,0,0,0,0,0]]
assert coup_possible(gril,0)==False
assert coup_possible(gril,6)==True

def vert(gril,j,lig,col):
    '''Détermine si il y a un alignement vertical de 4 pions du joueur j à partir de la case (lig, col)'''
    if lig>2 :
        return False
    else : 
        if j==1 : 
            for i in range(0,4) :
                if gril[lig+i][col]!=1 :
                    return False
            return True
        if j==2 : 
            for i in range(0,4) :
                if gril[lig+i][col]!=2 :
                    return False
            return True
        
gril=[[0,0,0,0,0,0,0],
      [0,1,0,0,0,0,1],
      [0,2,0,0,0,0,1],
      [0,2,0,0,0,0,1],
      [0,2,0,0,0,0,1],
      [0,0,0,0,0,0,0]]
assert vert(gril,1,1,6)==True
assert vert(gril,2,1,1)==False


def horiz(gril,j,lig,col) :
    '''
    Détermine si il y a un alignement horizontal de 4 pions du joueur j à partir de la case (lig,col).
    Renvoie True si c'est le cas, False dans le cas contraire.
    '''
    if col>3 :
        False
    else :
        if j==1 : 
            for i in range(0,4) :
                if gril[lig][col+i]!=1 :
                    return False
            return True
        if j==2 : 
            for i in range(0,4) :
                if gril[lig][col+i]!=2 :
                    return False
            return True
gril=[[0,0,0,2,2,2,2],
      [2,0,1,1,1,1,0],
      [2,0,0,0,0,0,0],
      [2,0,0,0,0,0,0],
      [2,0,0,0,0,0,0],
      [2,0,0,0,0,0,0]]
assert horiz(gril,1,1,2)==True
assert horiz(gril,2,0,3)==True
assert horiz(gril,1,4,2)==False


def diag_haut(gril,j,lig,col) :
    '''
    Détermine si il y a un alignement diagonal vers le haut
    de 4 pions du joueur j à partir de la case (lig,col).
    Renvoie True si oui, False sinon.
    '''
    if lig<2 or col>3 :
        return False
    else :
        if j==1 :
            for i in range(0,4):
                if gril[lig-i][col+i]!=1 :
                    return False
            return True
        if j==2 :
            for i in range(0,4):
                if gril[lig-i][col+i]!=2 :
                    return False
            return True
gril=[[0,0,0,0,2,0,2],
      [0,0,0,2,0,0,1],
      [0,0,2,0,0,1,1],
      [0,2,0,0,1,1,0],
      [0,0,0,0,1,0,0],
      [0,0,0,1,0,0,0]]
assert diag_haut(gril,2,3,1)==True
assert diag_haut(gril,1,5,3)==True
assert diag_haut(gril,2,3,4)==False
assert diag_haut(gril,2,0,6)==False


def diag_bas(gril,j,lig,col) :
    '''
    Détermine si il y a un alignement diagonal vers le bas
    de 4 pions du joueur j à partir de la case (lig,col).
    Renvoie True si oui, False sinon.
    '''
    if lig>2 or col>3 :
        return False
    else :
        if j==1 :
            for i in range(0,4):
                if gril[lig+i][col+i]!=1 :
                    return False
            return True
        if j==2 :
            for i in range(0,4):
                if gril[lig+i][col+i]!=2 :
                    return False
            return True
gril=[[0,0,0,0,0,0,0],
      [0,0,0,0,0,0,1],
      [2,0,0,1,0,0,2],
      [0,2,0,0,1,0,0],
      [0,0,2,0,0,1,0],
      [0,0,0,2,0,0,1]]
assert diag_bas(gril,1,2,3)==True
assert diag_bas(gril,2,2,0)==True
assert diag_bas(gril,2,0,4)==False
assert diag_bas(gril,2,4,6)==False


def victoire(gril,j) :
    '''
    Renvoit un bollén True si le joueur j a gagné, False sinon.
    '''
    for y in range(0,6):
        for x in range(0,7):
            if horiz(gril,j,y,x)==True :
                return True
            if vert(gril,j,y,x)==True :
                return True
            if diag_haut(gril,j,y,x)==True :
                return True
            if diag_bas(gril,j,y,x)==True :
                return True
    return False
gril=[[0,0,0,0,0,1,0],
      [0,0,0,0,1,0,0],
      [0,0,0,1,0,0,0],
      [0,0,1,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0]]
    
    
from random import randint       
def coup_aleatoire(gril,j):
    '''
    Joue un coup aléatoire pour le joueur j. On suppose la grille non pleine.
    '''
    flag=False
    while flag!=True :
        col=randint(0,6)
        if coup_possible(gril,col)==True :
            flag=True
            jouer(gril,j,col)


def jouer(gril,j,col):
    '''
    Fonction qui joue un coup du joueur j dans la colone col de la grille.
    '''
    flag=False
    index=[5,4,3,2,1,0]
    for i in index :
        if gril[i][col]==0 :
            gril[i][col]=j
            return None
            

def match_nul(gril):
    '''
    Renvoie True si la partie est nulle, c'est à dire si la ligne du haut est remplie, False sinon.
    '''
    for i in gril[0]:
        if i==0 :
            return False
    return True
gril=[[2,1,1,2,1,1,2],
      [2,0,0,0,0,0,0],
      [2,0,0,0,0,0,0],
      [2,0,0,0,0,0,0],
      [2,0,0,0,0,0,0],
      [2,0,0,0,0,0,0]]
assert match_nul(gril)==True

            
def affiche(gril):
    trad=[]
    final=[]
    for i in gril :
        for x in i :
            if x==0 :
                trad.append(".")
            if x==1 :
                trad.append("x")
            if x==2 :
                trad.append("0")
        final.append(trad)
        trad=[]
    for i in final :
        print(i)
gril=[[1,0,0,1,0,0,0],
      [0,0,0,2,0,0,0],
      [0,0,0,1,0,0,0],
      [0,0,0,2,0,0,0],
      [0,0,0,1,0,0,0],
      [0,0,0,2,0,0,0]]

import sys
typejeu=str(input("2J ou bien 1J  : "))
if typejeu=="2J" :
    gril=grille_vide()
    affiche(gril)
    while True:
        if victoire(gril,2)==True :
            print("Le J2 a gagné !")
            sys.exit()
        coup=int(input("Joueur 1, dans quelle index de colone jouer : "))
        while coup_possible(gril,coup)==False :
            print("Colone pleine !")
            coup=int(input("Joueur 1, dans quelle index de colone jouer : "))
        jouer(gril,1,coup)
        affiche(gril)
        if victoire(gril,1)==True :
            print("Le joueur 1 a gagné !")
            sys.exit()
        coup=int(input("Joueur 2, dans quelle index de colone jouer : "))
        while coup_possible(gril,coup)==False :
            print("Colone pleine !")
            coup=int(input("Joueur 2, dans quelle index de colone jouer : "))
        jouer(gril,2,coup)
        affiche(gril)
if typejeu=="1J" :
    gril=grille_vide()
    affiche(gril)
    while True:
        if victoire(gril,2)==True :
            print("Le robot a gagné !")
            sys.exit()
        coup=int(input("Joueur 1, dans quelle index de colone jouer : "))
        while coup_possible(gril,coup)==False :
            print("Colone pleine !")
            coup=int(input("Joueur 1, dans quelle index de colone jouer : "))
        jouer(gril,1,coup)
        affiche(gril)
        if victoire(gril,1)==True :
            print("Le joueur 1 a gagné !")
            sys.exit()
        print("Le robot joue.")
        coup_aleatoire(gril,2)
        affiche(gril)
