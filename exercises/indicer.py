__author__ = 'PWXG8293'


def indice(e, L=[]):
    a = 0
    while a < len(L):
        if e == L[a]:
            print("element ", e, "trouve a l'indice ", a)
            return a
        else:
            a = a + 1
    if a == len(L):
        print("element ", e, "non trouve dans la liste!!")
        return -1

