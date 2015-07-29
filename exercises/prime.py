#!/usr/bin/python -tt
import math

__author__ = 'Alexis.Koalla@orange.com'


def primer(n):
    a = 2
    isprime = True;
    print("Determiner si ", n, "est un nombre premier");
    while a < math.sqrt(n) and isprime:
        isprime = not (n % a == 0)
        a = a + 1
        print(isprime)
    if isprime:
        print(n, "est un nombre premier")
    else:
        print(n, "n'est pas un nombre premier")