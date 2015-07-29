__author__ = 'root'
def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a>b:
       value=b
    else:
        value=a
    for i in range(value):
        if a%value==0 and b%value==0:
            return value
        value-=1

print 'PGDC 2,12=',gcdIter(2, 12)

print 'PGDC 6,12=',gcdIter(6, 12)

print 'PGDC 9,12=',gcdIter(9, 12)

print 'PGDC 17,12=',gcdIter(17, 12)

print 'PGDC 10,5=',gcdIter(10, 5)

print 'PGDC (90, 144)',gcdIter(90, 144)