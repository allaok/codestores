__author__ = 'root'
def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    tuple_list=list(aTup)
    print tuple_list
    result=list()
    for e in tuple_list:
        print 'index=',tuple_list.index(e),'e=',e
        if tuple_list.index(e)%2==1:
           tuple_list.remove(e)
    return  aTup[::2]
a=('I', 'am', 'a', 'test', 'tuple')
print oddTuples(a)
print oddTuples((3, 7, 12, 10))
print oddTuples((20, 9, 19, 10, 1, 9, 10, 1, 4, 10))
#(20, 19, 1, 10, 4)

def oddTuples2(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    rTup = ()
    index = 0

    # Idea: Iterate over the elements in aTup, counting by 2
    #  (every other element) and adding that element to
    #  the result
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2

    return rTup