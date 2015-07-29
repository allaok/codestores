__author__ = 'Alexis.Koalla@orange.com'


def quicksort(L=[]):
    less = []
    equal = []
    greater = []
    if len(L) > 1:
        pivot = L[0]
        for x in L:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
    else:
        return L

    return quicksort(less) + equal + quicksort(greater)