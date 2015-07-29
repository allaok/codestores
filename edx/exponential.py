__author__ = 'root'
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    exponential=1
    while  exp >0:
        exponential= exponential*base
        exp -=1
    return exponential

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp ==0:
        return 1
    else:
        return base*recurPower(base,exp-1)

print recurPower(-8.3,0)
print recurPower(2,2)

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp==0 :
        return 1
    elif exp >0 and exp%2==0:
         return recurPowerNew(base*base, exp/2)
    elif exp >0 and exp%2==1:
         return base*recurPowerNew(base, exp-1)

print recurPowerNew(-8.3,0)
print recurPowerNew(2,2)
print recurPowerNew(-5.56, 3)