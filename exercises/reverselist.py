__author__ = 'PWXG8293'


def reverse(L=[]):
    l = len(L)
    l1 = []
    i = 0
    while i < l:
        l1.append(L[l - 1 - i])
        i += 1
    return l1;


