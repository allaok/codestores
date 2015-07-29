#!/usr/bin/python -tt
__author__ = 'Alexis.Koalla@orange.com'


def isPerfect(n):
    a = 1
    s = 0
    while a < n:
        if n % a == 0:
            s = s + a
        a = a + 1
    if n == s:
        return True
    else:
        return False


def perfects(n):
    print("Nombres parfaits inferieurs ou egaux a  ", n)
    a = 1
    while a <= n:
        if isPerfect(a):
            print (a),
        a += 1