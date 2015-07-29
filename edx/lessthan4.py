__author__ = 'root'
def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    result=list()
    for s in aList :
        if len(s)< 4:
            result.append(s )

    return  result

print lessThan4(["apple", "cat", "dog", "banana"])

