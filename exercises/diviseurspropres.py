#!/usr/bin/python -tt
__author__ = 'Alexis.Koalla@orange.com'


def dividers(n):
    a = 1
    dliste = []
    print("recherche des divieurs de", n);
    while a < n:
        if n % a == 0:
            dliste.append(a)
        a = a + 1
    print("Liste des diviseurs de", n, dliste)