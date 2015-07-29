 # Paste your code into this box
s='azcbobobobegghakl'
s = 'bobobbbobobehoboobobbjobbobob'
s2='bobbbobbbob'

i=0
cpt=0
print(s)
trouve=False
while i< len(s)-2:

    souschaine=s[i:i+3]
    #print 'souschaine==>', souschaine
    if souschaine== 'bob':
          cpt+=1
          #print 'souschaine: ',souschaine, i, i+3

    i+=1

print 'Number of times bob occurs is:',cpt





