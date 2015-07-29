__author__ = 'PWXG8293'

from math import ceil


def payer(resultat, choix, mise):
    gain = 0
    if resultat % 2 == choix % 2:  # le resultat du lancer est le choix du joueur ont la meme parite
        if choix == resultat:  # le resultat du lancer et la mise du jour sont identique
            gain = gain * 4  # le joueur remporte 3 fois la mise + la mise initiale
        else:
            gain = ceil(gain * 3 / 2)  # le joueur remporte la moitie de sa mise initiale +sa mise initiale
    return gain