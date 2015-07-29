__author__ = 'PWXG8293'


def dicho(element, liste_triee):
    if len(liste_triee) == 1:
        return 0
    m = len(liste_triee) // 2
    if liste_triee[m] == element:
        return m
    elif liste_triee[m] > element:
        return dicho(element, liste_triee[:m])
    else:
        return m + dicho(element, liste_triee[m:])
