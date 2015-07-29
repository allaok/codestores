__author__ = 'root'
def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N < 10:
        return N
    else:
        last_digit=N%10
        return last_digit+sumDigits((N-last_digit)/10)



print sumDigits(123456)
print sumDigits(12345)
