__author__ = 'PWXG8293'
import donnes
from random import randrange
import os


def choisirMot():
    index = randrange(len(donnes.mots))
    return donnes.mots[index]


def chooseLetter():
    lettre = input("Entrer une lettre: ")


