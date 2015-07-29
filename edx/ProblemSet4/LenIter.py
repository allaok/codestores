__author__ = 'root'
def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    index=0
    try:
        while aStr[index]:
           # print aStr[index]
            index+=1
    except IndexError,ie:
        index-=1
    return index+1

print "lenght=",lenIter('123456789')
print "lenght=",lenIter('1234567890')