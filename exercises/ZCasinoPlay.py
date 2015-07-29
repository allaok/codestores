__author__ = 'PWXG8293'
from random import *
import os

import ZCasino

argent = 500  # somme initiale du joueur
print ("===debut du jeu===")
gocasino = True
while gocasino:

    choix = -1
    while choix < 0 or choix > 49:
        choix = input("Entrer votre numero  dans [0,49] ")
        try:
            choix = int(choix)
        except ValueError:
            print("Veuillez ntrer un nombre dans [0,49]")
            choix = -1

    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Entrer votre mise:  ")
        try:
            mise = int(mise)
        except ValueError:
            print("Veuillez entrer un nombre entre 0 et ", argent)
            mise = 0

    numerogagnant = randrange(50)

    gain = ZCasino.payer(numerogagnant, choix, mise)
    if gain > 0:
        print("Vous avez gagne :%d", gain)
        argent += gain
    else:
        argent -= mise
        print("Vous avez perdu")
    print("Votre choix: ", choix, "Numero gagnant :", numerogagnant, "Votre mise: ", mise, " Vous avez : ", argent, "$")

if argent <= 0:
    print("Vous etes ruine", argent, "$")
    gocasino = False
quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
if quitter == "o" or quitter == "O":
    print("Vous quittez le casino avec vos gains.")
    gocasino = False
