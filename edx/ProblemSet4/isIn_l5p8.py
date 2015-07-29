__author__ = 'root'
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    nb_elemnts=len(aStr)
    print'NB Elements=',nb_elemnts,'aSTr= ', aStr
    if nb_elemnts==0:
        return False
    elif nb_elemnts==1 and char==aStr[0]:
        return True
    elif char==aStr[nb_elemnts/2]:
        return True
    elif char < aStr[nb_elemnts/2]:
        return isIn(char,aStr[:nb_elemnts/2])
    else:
        return isIn(char,aStr[nb_elemnts/2+1:nb_elemnts])

print isIn('d','abcdefg')
print isIn('h','abcdefg')
print isIn('y', 'achjmmprsstuxxyz')