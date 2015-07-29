__author__ = 'root'
def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    print a,b
    if b==0:
            return a
    else:
            return gcdRecur(b,a%b)

print 'PGDC 2,12=',gcdRecur(2, 12)

print 'PGDC 6,12=',gcdRecur(6, 12)

print 'PGDC 9,12=',gcdRecur(9, 12)

print 'PGDC 17,12=',gcdRecur(17, 12)

print 'PGDC 10,5=',gcdRecur(10, 5)

print 'PGDC (90, 144)',gcdRecur(90, 144)