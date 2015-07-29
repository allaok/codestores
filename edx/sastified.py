__author__ = 'root'
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    # Your function implementation here
    for s in L[:]:
        if not f(s):
            L.remove(s)
    return len(L)

def f(s):
    return 'a' in s

L = ['a', 'b', 'a']

print satisfiesF(L)
print L

L1 = ['a', 'b', 'a', 'ab', 'c', 'ac']

print satisfiesF(L1)
print L1

L11 = []

print satisfiesF(L11)
print L11

l=['abc', 'def', 'gha']
l2=['b']
print satisfiesF(l2)
print l2


#2
#['a', 'a']

#run_satisfiesF(L, satisfiesF)

