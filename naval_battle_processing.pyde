"""
test
Version 2 dimension
Fonction NouveauPlateau
Michel
Amine
"""

import random
import copy
import time

game = False
def setup():
    global grille, deathstar, intercepteur, TIE, superdestroyer, croiseur, explosion, rate
    grille = loadImage("grille.png")
    deathstar = loadImage("etoiledelamort.png")
    intercepteur = loadImage("intercepteur.png")
    TIE = loadImage("TIE.png")
    superdestroyer = loadImage("superdestroyer.png")
    croiseur = loadImage("croiseur.png")
    explosion = loadImage("BOOM.png")
    rate = loadImage("rate.png")
    size(800,800)
check = False
partie = False
tours = "joueur"
def draw():
    if game == False:
        textFont(createFont("taille", 40))
        text("Star Wars", 100, 120)
        textFont(createFont("taille", 40))
        text("SQUADRON", 70, 160)
def mouseReleased():
    global game
    if game == False:
        if (mouseX >100 and mouseX <800 and mouseY > 120 and mouseY < 800):
            rect(0, 800,0, 800)
            time.sleep(1) # Temps de transition entre menu et jeu
            fill(0)
            rect(0, 0, 800, 800)
            stroke(255)
            rect(0, 300, 300, 100)
            stroke(255)
            rect(500, 300, 300, 100)
            textFont(createFont("taille", 40))
            fill(255)
            text("PLAYER", 70, 360)
            textFont(createFont("taille", 40))
            fill(255)
            text("ORDI", 570, 360)
            affichage()
            game = True
    if game == True:
        LancerPartie(10)
        
        
    if (mouseX >0 and mouseX <10 and mouseY > 0 and mouseY < 10):
        exit()

def affichage():
    image(grille, 0, 0, 300, 300)
    image(grille, 500, 0, 300, 300)
    image(deathstar, 300, 20, 200, 280)

            
        
# Les images en caractères
to = " X " #touché
ra = "███" #raté
ca = "▒▒▒" #case vide
cuirasse_char = "cui"
croiseur_char = "cro"
torpilleur_char = "tor"
sous_marin_char = "sou"
ba = " ◯" #case d'un navire

list_char_bateaux = [cuirasse_char,croiseur_char,torpilleur_char,sous_marin_char]

vie_joueur = {
    "cui" : 4,
    "cro" : 3,
    "tor" : 2,
    "sou" : 1
}

vie_ordi = {
    "cui" : 4,
    "cro" : 3,
    "tor" : 2,
    "sou" : 1
}

taille_bateaux = {
    "cui" : 4,
    "cro" : 3,
    "tor" : 2,
    "sou" : 1
}

nom_bateaux = {
    "cui" : "cuirasse",
    "cro" : "croiseur",
    "tor" : "torpilleur",
    "sou" : "sous marin"
}


# Les tailles des vaisseaux
taille_cuirasse = 4
taille_croiseur = 3
taille_torpilleur = 2
taille_sous_marin = 1


# Nombre de cases de long du plateau (carré)
def NouveauPlateau(nbCases): #Test fonction

    if nbCases < 10:
        print("Le nombre de cases demandé est trop petit. Un plateau de 10 cases par defaut vous a été retourné")
        nbCases = 10

    plateau = []
    for ligne in range(nbCases):
        plateau_ligne = [ca] * nbCases
        plateau.append(plateau_ligne)

    #Cuirasse
    lol = random.randint(0, 1)

    #Placement vertical
    if lol == 1:
        indice_cuirassever = random.randint(0, nbCases - taille_cuirasse)
        indice_cuirassehor = random.randint(0, nbCases - 1)
        for i in range(indice_cuirassever, indice_cuirassever + taille_cuirasse):
            plateau[i][indice_cuirassehor] = cuirasse_char
    #Placement horizontal
    else:
        indice_cuirassever = random.randint(0, nbCases)
        indice_cuirassehor = random.randint(0, nbCases - taille_cuirasse)
        for i in range(indice_cuirassehor, indice_cuirassehor + taille_cuirasse):
            plateau[indice_cuirassever-1][i] = cuirasse_char

    #Placer le croiseur
    lol = random.randint(0,1)
    placement_reussi = False

    while not placement_reussi:
        if lol == 1:
            bool = 0
            indice_croiseurver = random.randint(0, nbCases - taille_croiseur)
            indice_croiseurhor = random.randint(0, nbCases - 1)
            for i in range(indice_croiseurver, indice_croiseurver + taille_croiseur):
                if plateau[i][indice_croiseurhor] == ca:
                    bool += 1
            if bool == 3:
                placement_reussi = True
                for i in range(indice_croiseurver, indice_croiseurver + taille_croiseur):
                    plateau[i][indice_croiseurhor] = croiseur_char
        else:
            bool = 0
            indice_croiseurver = random.randint(0, nbCases - 1)
            indice_croiseurhor = random.randint(0, nbCases - taille_croiseur)
            for i in range(indice_croiseurhor, indice_croiseurhor + taille_croiseur):
                if plateau[indice_croiseurver][i] == ca:
                    bool += 1
            if bool == 3:
                placement_reussi = True
                for i in range(indice_croiseurhor, indice_croiseurhor + taille_croiseur):
                    plateau[indice_croiseurver][i] = croiseur_char

    #placer torpilleur
    lol = random.randint(0, 1)
    placement_reussi = False

    while not placement_reussi:
        if lol == 1:
            bool = 0
            indice_torpilleurver = random.randint(0, nbCases - taille_torpilleur)
            indice_torpilleurhor = random.randint(0, nbCases - 1)
            for i in range(indice_torpilleurver, indice_torpilleurver + taille_torpilleur):
                if plateau[i][indice_torpilleurhor] == ca:
                    bool = bool + 1
            if bool == 2:
                placement_reussi = True
                for i in range(indice_torpilleurver, indice_torpilleurver + taille_torpilleur):
                    plateau[i][indice_torpilleurhor] = torpilleur_char
        else:
            bool = 0
            indice_torpilleurver = random.randint(0, nbCases - 1)
            indice_torpilleurhor = random.randint(0, nbCases - taille_torpilleur)
            for i in range(indice_torpilleurhor, indice_torpilleurhor + taille_torpilleur):
                if plateau[indice_torpilleurver][i] == ca:
                    bool += 1
            if bool == 2:
                placement_reussi = True
                for i in range(indice_torpilleurhor, indice_torpilleurhor + taille_torpilleur):
                    plateau[indice_torpilleurver][i] = torpilleur_char


    #placer sous marin
    lol = random.randint(0, 1)
    placement_reussi = False

    while not placement_reussi:
        if lol == 1:
            bool = 0
            indice_sous_marinver = random.randint(0, nbCases - taille_croiseur)
            indice_sous_marinhor = random.randint(0, nbCases - 1)
            for i in range(indice_sous_marinver, indice_sous_marinver + taille_sous_marin):
                if plateau[i][indice_sous_marinhor-1] == ca:
                    bool += 1
            if bool == 1:
                placement_reussi = True
                for i in range(indice_sous_marinver, indice_sous_marinver + taille_sous_marin):
                    plateau[i][indice_sous_marinhor] = sous_marin_char
        else:
            bool = 0
            indice_sous_marinver = random.randint(0, nbCases - 1)
            indice_sous_marinhor = random.randint(0, nbCases - taille_sous_marin)
            for i in range(indice_sous_marinhor, indice_sous_marinhor + taille_sous_marin):
                if plateau[indice_sous_marinver][i] == ca:
                    bool += 1
            if bool == 1:
                placement_reussi = True
                for i in range(indice_sous_marinhor, indice_sous_marinhor + taille_sous_marin):
                    plateau[indice_sous_marinver][i] = sous_marin_char

    return plateau

def AfficherPlateau(plateau, monPlateau):
#rappel de la liste: list_char_bateaux = [cuirasse_char,croiseur_char,torpilleur_char,sous_marin_char]
    globals()["c0"]= 2
    globals()["c1"]= 32
    globals()["c2"]= 62
    globals()["c3"]= 92
    globals()["c4"]= 122
    globals()["c5"]= 152
    globals()["c6"]= 182
    globals()["c7"]= 212
    globals()["c8"]= 242
    globals()["c9"]= 272
    if monPlateau == True:
        plateau_copie_joueur = copy.deepcopy(plateau)
        for i in range(0,len(plateau_copie_joueur)):
            for j in range(0,len(plateau_copie_joueur)):
                if plateau_copie_joueur[i][j] in list_char_bateaux:
                    plateau_copie_joueur[i][j] = ba
                    if plateau_copie_joueur[i][j] == list_char_bateaux[0]:
                        image(superdestroyer, globals()["c"+ str(j)], globals()["c"+ str(i)], 28, 28)
                    if plateau_copie_joueur[i][j] == list_char_bateaux[1]:
                        image(croiseur, globals()["c"+ str(j)], globals()["c"+ str(i)], 28, 28)                        
                    if plateau_copie_joueur[i][j] == list_char_bateaux[2]:
                        image(intercepteur, globals()["c"+ str(j)], globals()["c"+ str(i)], 28, 28)
                    if plateau_copie_joueur[i][j] == list_char_bateaux[3]:
                        image(TIE, globals()["c"+ str(j)], globals()["c"+ str(i)], 28, 28)
        for case in plateau_copie_joueur:
            print(case)

    else:
        plateau_copie_ordi = copy.deepcopy(plateau)
        for i in range(0,len(plateau_copie_ordi)):
            for j in range(0,len(plateau_copie_ordi)):
                if plateau_copie_ordi[i][j] in list_char_bateaux:
                    plateau_copie_ordi[i][j] = ca
        for case in plateau_copie_ordi:
            print(case)


def EstTermine(plateau):
    for  ligne in plateau:
        for case in ligne:
            if case in list_char_bateaux:
                return False
    return True


# verifier que l entrée est un nombre, entre 0 et nombre de case, si l'entree de l utilsiateur est mauvaise alors reboucler pour lui demander de corriger, la case bateau doit se transformer en touché, la case vide en plouf, les autres doivent rester les meme,
def RealiserChoixJoueur(plateau):
    globals()["c0"]= 502
    globals()["c1"]= 532
    globals()["c2"]= 562
    globals()["c3"]= 592
    globals()["c4"]= 622
    globals()["c5"]= 652
    globals()["c6"]= 682
    globals()["c7"]= 712
    globals()["c8"]= 742
    globals()["c9"]= 772


    globals()["a0"]= 2
    globals()["a1"]= 32
    globals()["a2"]= 62
    globals()["a3"]= 92
    globals()["a4"]= 122
    globals()["a5"]= 152
    globals()["a6"]= 182
    globals()["a7"]= 212
    globals()["a8"]= 242
    globals()["a9"]= 272
    
    
    def mousePressed():
        ligne_choisi = round((mouseX - 500)/30) # 30px est la mesure d'un côté d'une case
        colonne_choisi = round(mouseY/30) # 30px est la mesure d'un côté d'une case
        ligne_choisi = int(ligne_choisi)
        colonne_choisi = int(colonne_choisi)
        if plateau[ligne_choisi][colonne_choisi] == to or plateau[ligne_choisi][colonne_choisi] == ra:
            print("Vous avez tiré sur une case qui a déjà été ciblé.")
        else:
            if plateau[ligne_choisi][colonne_choisi] in list_char_bateaux:
                print("BOOM")
                vie_ordi[plateau[ligne_choisi][colonne_choisi]] -= 1
                if vie_ordi[plateau[ligne_choisi][colonne_choisi]] == 0:
                    print("Vous avez coulé le {nom_bateaux[plateau[ligne_choisi -1 ][colonne_choisi - 1]]} de l'ordinateur")
                image(explosion, globals()["c" + str(ligne_choisi)], globals()["a" + str(colonne_choisi)], 28, 28)
                plateau[ligne_choisi][colonne_choisi] = to
            else:
                print("PLOUF")
                image(rate, globals()["c" + str(ligne_choisi)], globals()["a" + str(colonne_choisi)], 28, 28)
                plateau[ligne_choisi][colonne_choisi] = ra
        choose = 0
    

def RealiserChoixOrdinateur(plateau):
    globals()["c0"]= 2
    globals()["c1"]= 32
    globals()["c2"]= 62
    globals()["c3"]= 92
    globals()["c4"]= 122
    globals()["c5"]= 152
    globals()["c6"]= 182
    globals()["c7"]= 212
    globals()["c8"]= 242
    globals()["c9"]= 272
    ligne_choisi = random.randint(0,len(plateau)-1)
    colonne_choisi = random.randint(0,len(plateau[ligne_choisi])-1)
    while plateau[ligne_choisi][colonne_choisi] == to or plateau[ligne_choisi][colonne_choisi] == ra:
        ligne_choisi = random.randint(0,len(plateau)-1)
        colonne_choisi = random.randint(0,len(plateau[ligne_choisi])-1)
    if plateau[ligne_choisi][colonne_choisi] in list_char_bateaux :
        print("L'ordinateur a touché votre {nom_bateaux[plateau[ligne_choisi][colonne_choisi]]}!")
        vie_joueur[plateau[ligne_choisi][colonne_choisi]] -= 1
        if vie_joueur[plateau[ligne_choisi][colonne_choisi]] == 0:
            print("BOUM votre {nom_bateaux[plateau[ligne_choisi][colonne_choisi]]} a été coulé !")
        image(explosion, globals()["c" + str(ligne_choisi)], globals()["c" + str(colonne_choisi)], 28, 28) # Peut-être défaillance dans cette ligne, à voir...
        plateau[ligne_choisi][colonne_choisi] = to
        
    else:
        print("L'ordinateur a raté son coup")
        image(rate, globals()["c" + str(ligne_choisi)], globals()["c" + str(colonne_choisi)], 28, 28)
        plateau[ligne_choisi][colonne_choisi] = ra

        

def LancerPartie(nbCases):
    plateauJoueur = NouveauPlateau(nbCases)
    plateauOrdi = NouveauPlateau(nbCases)
    
    print("Les plateaux ont été crées, la partie est lancée")
    tours = "joueur"
    while EstTermine(plateauJoueur) == False and EstTermine(plateauOrdi) == False:
        if tours == "joueur":
            print("C'est votre tour, voici le plateau de l'ordinateur:")
            AfficherPlateau(plateauOrdi, False)
            RealiserChoixJoueur(plateauOrdi)
            AfficherPlateau(plateauOrdi, False)
            tours = "ordi"
            if EstTermine(plateauOrdi):
                print("La partie est terminée, vous avez gagné!!!")
        elif tours == "ordi":
            print("C'est à l'ordinateur de jouer, voici votre plateau:")
            AfficherPlateau(plateauJoueur, True)
            RealiserChoixOrdinateur(plateauJoueur)
            AfficherPlateau(plateauJoueur, True)
            tours = "joueur"
            if EstTermine(plateauJoueur):
                print("La partie est terminée, vous avez perdu...")
        time.sleep(3)
        
