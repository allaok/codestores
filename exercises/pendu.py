__author__ = 'PWXG8293'

import donnes
import penduUtils
import os

player = ""
print("ENtrer votre pseudo: ")
player = input()
player = str(player)
motadeviner = penduUtils.choisirMot()

trouve = False
motdeviner = ["*"] * 8
cpt = 0
i = 0
restant = donnes.nombre_chance
while not trouve and cpt <= donnes.nombre_chance:
    lettre = penduUtils.chooseLetter()
    assert chr(lettre)
    while i < len(motadeviner):
        if motadeviner[i] == lettre:
            motdeviner[i] = lettre
            restant -= 1
            print("Etat du pendu: ", motdeviner)
        i += 1
    cpt += 1
    trouve = restant == 0
with open("repo/" + donnes.nom_fichier_scores, "arw") as scores:
    scores.write((player, donnes.nombre_chance - cpt))
    scores.close()





