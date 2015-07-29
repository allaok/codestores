__author__ = 'root'
#L3 PROBLEM 5A  (2/2 points)
#In this problem you'll be given a chance to practice writing some for loops.

#1. Convert the following code into code that uses a for loop.
i=1
for i in range(1,6):
    print i*2
    i+=1
print 'Goodbye!'

#L3 PROBLEM 5B  (2/2 points)
#2. Convert the following code into code that uses a for loop.
i=1
print 'Hello!'
for i in range(1,6):
    print (6-i)*2
    i-=1

#L3 PROBLEM 5C  (3/3 points)
#. Write a for loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:
end=10
i=1
cpt=0
for i in range(1,end+1):
    cpt+=i
    i+=1
print cpt

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Your code here
    return max(lo,min(x,hi))


def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    return char in ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']

def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    return char== 'a' or char =='e' or char=='i' or char=='u' or char=='o' or char== 'A' or char =='E' or char=='I' or char=='U' or char=='O'

def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return x%2==1

def square(x):
    return x*x

def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    return square(x)*square(x)
