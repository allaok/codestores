__author__ = 'root'
# Paste your function here
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    l=1
    base=0
    while l<= x:
        print 'l= ',l, 'base= ',base
        l=l*b
        if l<= x:
           base=base+1


    print base

myLog(16,2)
myLog(15,3)
myLog(7,3)
myLog(7,2)

