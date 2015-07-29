__author__ = 'root'
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggers=dict()
    # Your Code Here
    if len(aDict.keys())==0:
        return None
    else:
        for key in aDict.keys():
            biggers[key]=len(aDict[key])
    big_value=max(biggers.values())
    for b in biggers.keys():
        if biggers[b]== big_value:
            return b


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print biggest(animals)