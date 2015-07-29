__author__ = 'root'
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here
    result=list()
    for key in aDict.keys() :
        print 'key =',key, 'value= ',aDict[key]
        if aDict[key] == target :
            result.append(key)
    result.sort()
    return result

print keysWithValue({},0)
print keysWithValue({2:0,3:0},0)