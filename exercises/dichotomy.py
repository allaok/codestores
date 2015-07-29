#!/usr/bin/python -tt
__author__ = 'Alexis.Koalla@orange.com'


def dichotomic(e, l):
    longueur = len(l) // 2
    if e == l[longueur]:
        print(l)
        return longueur
    elif l[longueur] > e:
        print(l)
        return dichotomic(e, l[:longueur])
    else:
        print(l)
        indice = longueur + dichotomic(e, l[longueur:])
        print("element ", e, "trouve a l'index:", indice)
        return indice

