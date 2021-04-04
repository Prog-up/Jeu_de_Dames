
#======================================================================
# Projet-NSI-1ère.py	Prog_up	 2020-05-07
#
#======================================================================

#----------------------------------------------------------------------
# Import
from math import *

#======================================================================
# Definition des fonctions.

#----------------------------------------------------------------------
# Definie l'introduction.
def introduction() :
    return "\nBonjour et bienvenue sut cette simulation du jeu de dame !\nPour jouer, il vous suffit de donner la position de votre pion sur l'axe des abscisses X, puis sur l'axe des ordonnées Y.\nEnsuite pour avez le choix entre 4 actions :\n  Hd pour aller en Haut à droite ;\n  Hg pour aller en Haut à gauche ;\n  Bd pour aller en Bas à droite ;\n  Bg pour aller en Bas à gauche.\n"

#----------------------------------------------------------------------
# Définie les pions adverses.
def pionAdv(pion) :
    if pion == "⬤" :
        return "◎"
    else :
        return "⬤"

def pionAdvDame(pionD) :
    if pionD == "★":
        return "☆"
    else :
        return "★"

#----------------------------------------------------------------------
# Demande à répéter l'intrduction.
def demandeIntro(reponse):
    if reponse == "oui" :
        print(introduction())

#----------------------------------------------------------------------
# Envoie d'un msg en cas d'action impossible.
def erreur():
    if attaqueEnSerie == False :
        print("\nAction impossible\n")
        return False
    else :
        print("\nIl n'y a pas de pion à attaquer !")
        return True

#----------------------------------------------------------------------
# Permet de s'attaquer à un second pion au même tour.
def verificationNouvelleAttaquePossible(positionY, positionX, m) :
    print(positionY, positionX)
    if m[positionY + 1][positionX + 1] == pionAdv(pion) and m[positionY + 2][positionX + 2] == "⬜" or m[positionY + 1][positionX - 1] == pionAdv(pion) and m[positionY + 2][positionX - 2] == "⬜" or m[positionY - 1][positionX + 1] == pionAdv(pion) and m[positionY - 2][positionX + 2] == "⬜" or m[positionY - 1][positionX - 1] == pionAdv(pion) and m[positionY - 2][positionX - 2] == "⬜" :
        print("\nVous pouvez attaquer un nouvelle fois l'ennemi !\nVotre pion est en x :", positionX, "; y :", positionY)
        return True
    else :
        return False

#----------------------------------------------------------------------
# Recherche le nb d'objets selectionné dans la matrice.
def compteur(matrice, objet, nb = 0) :
    for i in range(11):
        if matrice[i].count(objet) != 0 :
                nb += 1
    return nb

#======================================================================
# Démarrage du jeu

#----------------------------------------------------------------------
# Introduction
print(introduction())

#----------------------------------------------------------------------
# Ajoute la numéroation verticale et les 9 première lignes du tableau.
t = ["{}  ".format(i) for i in range (2)]
for i in range (7) :
    t.append("{} ".format(2 + i))
for i in range (2) :
    t.append("{}".format(9 + i))
for i in range (9) :
    if i % 2 == 0 :
        t.append("{}  ".format(i + 1))
        for j in range (5) :
            t.append("⬛")
            t.append("⬜")            
    else :
        t.append("{}  ".format(i + 1))
        for j in range (5) :
            t.append("⬜")
            t.append("⬛")

#----------------------------------------------------------------------
# Ajoute la ligne 10 au tableau,
# ne comprenant pas d'espace après la numérotation.
t.append(10)
for j in range (5) :
    t.append("⬜")
    t.append("⬛")
    
#----------------------------------------------------------------------
# Ajoute 20 pions blancs.
for i in range (11, 54) :
    if t[i] == "⬜" :
        t[i] = "◎"

#----------------------------------------------------------------------
# Ajoute 20 pions noirs.
for i in range (len(t)-1, 78, -1) :
    if t[i] == "⬜" :
        t[i] = "⬤"

#----------------------------------------------------------------------
# Crée la matrice e de 10×10 dont les coefficients sont 0.
v = 11
m = [[0 for j in range(v)] for i in range(v)]

#----------------------------------------------------------------------
# Place le tableau t dans la matrice m.
k = 0
for i in range (v) :
    for j in range (v) :
        m[i][j] = t[k]
        k += 1
        
#----------------------------------------------------------------------
# Passe à la ligne entre chaque fin de tableau de la matrice m.
for i in m:
    for j in i:
        print(j, end='  ')
    print()
print()


#======================================================================
# Ensemble du jeu, comprend l'organisation des pions des 2 joueurs,
# leurs déplacements, transformation en Dames et la fin de la partie.

#----------------------------------------------------------------------
# Initialisation.
end = False
tour = 0
attaqueEnSerie = False
while end == False :
    joueur = 1
    tour += 1
    tourAttaqueEnSerie = 0
    while joueur != 3 :        
        if attaqueEnSerie == False :
            pionSelect = False
        deplacementSelect = False
        bordAtteint = False
        while deplacementSelect == False :
            while pionSelect == False :      
                if joueur == 1 :
                    pion = "⬤"
                    pionD = "★"
                else :
                    pion = "◎"
                    pionD = "☆"
                print("C'est au tour du joueur", joueur, "de jouer !\n")
                positionX = input("Quelle est ta position x ? ")
                positionY = input("Quelle est ta position y ? ")
                if positionY.isdigit() and positionX.isdigit() :
                    positionX = int(positionX)
                    positionY = int(positionY)
                    if positionY <= 10 and positionX <= 10 :
                        if m[positionY][positionX] == pion or m[positionY][positionX] == pionD :
                            pionSelect = True
                        else :                            
                            print("\nIl n'y a pas de pion !\n")
                    else :
                        print("\n/!\ Tu donnes une case inéxistante, ta position est trop grande et ne doit pas dépasser 10\n")
                else :
                    print("\nIl faut donner un nombre !\n")
            deplacement = input("Que veut tu faire ? ")
            
#======================================================================
# Choix d'une action celon les paramètres précedants :

#----------------------------------------------------------------------
# Pour une dame :
            if m[positionY][positionX] == pionD :

#----------------------------------------------------------------------
# Deplace la Dame en Bas à droite.
                if deplacement == "Bd" :
                    if positionY != 10 or positionX != 10 :
                        deplacementValide = False
                        for i in range(9):
                            if positionY + i == 10 or positionX + i == 10 :
                                if m[positionY + i][positionX + i] == "⬜" :
                                    deplacementValide = True
                        if deplacementValide == True :
                            bordAtteint = False
                            i = 0                            
                            while bordAtteint == False :
                                i += 1
                                if m[positionY + i][positionX + i] == pionAdv(pion) :
                                    m[positionY + i][positionX + i] = "⬜"
                                if positionY + i == 10 or positionX + i == 10 :
                                    m[positionY + i][positionX + i] = pionD
                                    bordAtteint = True
                        else :
                            pionSelect = erreur()   
                    else :
                            pionSelect = erreur()
                            
#----------------------------------------------------------------------
# Deplace la Dame en Bas à gauche.
                elif deplacement == "Bg" :
                    if positionY != 10 or positionX != 1 :
                        deplacementValide = False
                        for i in range(9):
                            if positionY + i == 10 or positionX - i == 1 :
                                if m[positionY + i][positionX - i] == "⬜" :
                                    deplacementValide = True
                        if deplacementValide == True :
                            bordAtteint = False
                            i = 0                            
                            while bordAtteint == False :
                                i += 1
                                if m[positionY + i][positionX - i] == pionAdv(pion) :
                                    m[positionY + i][positionX - i] = "⬜"
                                if positionY + i == 10 or positionX - i == 1 :
                                    m[positionY + i][positionX - i] = pionD
                                    bordAtteint = True
                        else :
                            pionSelect = erreur()  
                    else :
                            pionSelect = erreur()

#----------------------------------------------------------------------
# Deplace la Dame en Haut à droite.                           
                elif deplacement == "Hd" :
                    if positionY != 1 or positionX != 10 :
                        deplacementValide = False
                        for i in range(9):
                            if positionY - i == 1 or positionX + i == 10 :
                                if m[positionY - i][positionX + i] == "⬜" :
                                    deplacementValide = True
                        if deplacementValide == True :
                            bordAtteint = False
                            i = 0                            
                            while bordAtteint == False :
                                i += 1
                                if m[positionY - i][positionX + i] == pionAdv(pion) :
                                    m[positionY - i][positionX + i] = "⬜"
                                if positionY - i == 1 or positionX + i == 10 :
                                    m[positionY - i][positionX + i] = pionD
                                    bordAtteint = True
                        else :
                            pionSelect = erreur()
                    else :
                            pionSelect = erreur()

#----------------------------------------------------------------------
# Deplace la Dame en Haut à gauche.                            
                elif deplacement == "Hg" :
                    if positionY != 1 or positionX != 1 :
                        deplacementValide = False
                        for i in range(9):
                            if positionY - i == 1 or positionX - i == 1 :
                                if m[positionY - i][positionX - i] == "⬜" :
                                    deplacementValide = True
                        if deplacementValide == True :
                            bordAtteint = False
                            i = 0                            
                            while bordAtteint == False :
                                i += 1
                                if m[positionY - i][positionX - i] == pionAdv(pion) :
                                    m[positionY - i][positionX - i] = "⬜"
                                if positionY - i == 1 or positionX - i == 1 :
                                    m[positionY - i][positionX - i] = pionD
                                    bordAtteint = True
                        else :
                            pionSelect = erreur()  
                    else :
                            pionSelect = erreur()

#----------------------------------------------------------------------
# Demande au joueur si il a besoin d'aide au cas où il saisie un action invalide.                                
                else :
                    demandeIntro(input("\nAction inéxistante !\nVoulez-vous revoir l'introduction ? (oui/non) "))
                        
#----------------------------------------------------------------------
# Pour un pion normal :
            else :

#----------------------------------------------------------------------
# Deplace le pion en Bas à droite.
                if deplacement == "Bd" :
                    if positionY == 10 or positionX == 10 :
                        pionSelect = erreur()
                        actionExecute = False
                    else :
                        if m[positionY + 1][positionX + 1] == "⬜" and pion == "◎" and attaqueEnSerie == False :
                            m[positionY + 1][positionX + 1] = pion
                            if (positionY +1) == 10 :
                                m[positionY + 1][positionX + 1] = pionD
                            actionExecute = True
                        elif positionY != 9 and positionX != 9  :
                            if m[positionY + 1][positionX + 1] == pionAdv(pion) and m[positionY + 2][positionX + 2] == "⬜" :
                                m[positionY + 2][positionX + 2] = pion
                                m[positionY + 1][positionX + 1] = "⬜"
                                if (positionY + 2) == 10 and pion == "◎"  :
                                    m[positionY + 2][positionX + 2] = pionD
                                attaqueEnSerie = verificationNouvelleAttaquePossible(positionY + 2, positionX + 2, m)
                                actionExecute = True
                            else :
                                pionSelect = erreur()
                                actionExecute = False
                        else :
                            pionSelect = erreur()
                            actionExecute = False

#----------------------------------------------------------------------
# Deplace le pion en Bas à gauche.                            
                elif deplacement == "Bg" :
                    if positionY == 10 or positionX == 1 :
                        pionSelect = erreur()
                        actionExecute = False
                    else :
                        if m[positionY + 1][positionX - 1] == "⬜" and pion == "◎" and attaqueEnSerie == False :
                            m[positionY + 1][positionX - 1] = pion
                            if (positionY + 1) == 10 :
                                m[positionY + 1][positionX - 1] = pionD
                            actionExecute = True
                        elif positionY != 9 and positionX != 2  :
                            if m[positionY + 1][positionX - 1] == pionAdv(pion) and m[positionY + 2][positionX - 2] == "⬜" :
                                m[positionY + 2][positionX - 2] = pion
                                m[positionY + 1][positionX - 1] = "⬜"
                                if (positionY + 2) == 10 and pion == "◎"  :
                                    m[positionY + 2][positionX - 2] = pionD
                                attaqueEnSerie = verificationNouvelleAttaquePossible(positionY + 2, positionX - 2, m)
                                actionExecute = True
                            else :
                                pionSelect = erreur()
                                actionExecute = False
                        else :
                            pionSelect = erreur()
                            actionExecute = False

#----------------------------------------------------------------------
# Deplace le pion en Haud à droite.                            
                elif deplacement == "Hd" :
                    if positionY == 1 or positionX == 10 :
                        pionSelect = erreur()
                        actionExecute = False
                    else :
                        if m[positionY - 1][positionX + 1] == "⬜" and pion == "⬤" and attaqueEnSerie == False :
                            m[positionY - 1][positionX + 1] = pion
                            if (positionY - 1) == 1 :
                                m[positionY - 1][positionX + 1] = pionD
                            actionExecute = True
                        elif positionY != 2 and positionX != 9  :
                            if m[positionY - 1][positionX + 1] == pionAdv(pion) and m[positionY - 2][positionX + 2] == "⬜" :
                                m[positionY - 2][positionX + 2] = pion
                                m[positionY - 1][positionX + 1] = "⬜"
                                if (positionY - 2) == 1 and pion == "⬤"  :
                                    m[positionY - 2][positionX + 2] = pionD
                                attaqueEnSerie = verificationNouvelleAttaquePossible(positionY - 2, positionX + 2, m)
                                actionExecute = True
                            else :
                                pionSelect = erreur()
                                actionExecute = False
                        else :
                            pionSelect = erreur()
                            actionExecute = False


#----------------------------------------------------------------------
# Deplace le pion en Haud à gauche.                               
                elif deplacement == "Hg" :
                    if positionY == 1 or positionX == 1 :
                        pionSelect = erreur()
                        actionExecute = False
                    else :
                        if m[positionY - 1][positionX - 1] == "⬜" and pion == "⬤" and attaqueEnSerie == False :
                            m[positionY - 1][positionX - 1] = pion
                            if (positionY - 1) == 1 :
                                m[positionY - 1][positionX - 1] = pionD
                            actionExecute = True
                        elif positionY != 2 and positionX != 2  :
                            if m[positionY - 1][positionX - 1] == pionAdv(pion) and m[positionY - 2][positionX - 2] == "⬜" :
                                m[positionY - 2][positionX - 2] = pion
                                m[positionY - 1][positionX - 1] = "⬜"
                                if (positionY - 2) == 1 and pion == "⬤" :
                                    m[positionY - 2][positionX + 2] = pionD
                                attaqueEnSerie = verificationNouvelleAttaquePossible(positionY - 2, positionX - 2, m)
                                actionExecute = True
                            else :
                                pionSelect = erreur()
                                actionExecute = False
                        else :
                            pionSelect = erreur()
                            actionExecute = False

#----------------------------------------------------------------------
# Demande au joueur si il a besoin d'aide au cas où il saisie un action invalide.                            
                else :
                    demandeIntro(input("\nAction inéxistante !\nVoulez-vous revoir l'introduction ? (oui/non) "))

#----------------------------------------------------------------------
# Met un case vide à la fin du déplacement du pion ainsi que confirme le déplaacement du joueur et passe au joueur suivant
            if actionExecute == True :
                m[positionY][positionX] = "⬜"
                deplacementSelect = True
                tourAttaqueEnSerie += 1
                if attaqueEnSerie == False or tourAttaqueEnSerie == 2 :
                    joueur += 1
                    tourAttaqueEnSerie = 0
            
#----------------------------------------------------------------------
# Affiche la matrice à la fin de chaque tour.
        print()
        for i in m:
            for j in i:
                print(j, end=' ')
            print()
        print()

#----------------------------------------------------------------------
# Affiche nombre de tours.
    if end == False :
        print("Nous avons finit le tour", tour, "!")
        print()
        
#======================================================================
# Cherche si le jeu est finit.

#----------------------------------------------------------------------
# Recherche si un des joueurs à perdu.
        if compteur(m, pionAdv(pion)) == 0 and compteur(m, pionAdvDame(pionD)) == 0 or compteur(m, pionAdv(pion)) == 0 and compteur(m, pion) == 0 :
            if compteur(m, pionAdvDame(pionD)) > compteur(m, pionD) :
                end = True
                if joueur == 2 :
                    print("C'est le joueur 2 qui a gagné !\nLa partie à durée", tour, "tours !")
                else :
                    print("C'est le joueur 1 qui a gagné !\nLa partie à durée", tour, "tours !")
                joueur = 3
            else :
                end = True
                print("C'est le joueur", joueur - 1, "qui a gagné !\nLa partie à durée", tour, "tours !")
                joueur = 3
        
#----------------------------------------------------------------------
# Fin.  
print("\nFIN")
