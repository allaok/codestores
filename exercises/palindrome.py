#!/usr/bin/python -tt
__author__ = 'Alexis.Koalla@orange.com'


def palindrome(s):
    word = s;
    print("valeur initiale", word);
    if len(s) < 1:
        print("La chaine donnee est un palindrome!!")
    elif s[0] == s[len(s) - 1]:
        # print(s[0:len(s)-1])
        palindrome(s[1:len(s) - 1])
    else:
        print("La chaine donnee n'est pas un palindrome!")

   