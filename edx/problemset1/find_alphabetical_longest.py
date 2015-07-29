from itertools import count
s = 'azcbobobegghakl'
maxsubstr = s[0:0] # empty slice (to accept subclasses of str)
for start in range(len(s)): # O(n)
    for end in count(start + len(maxsubstr) + 1): # O(m)
        substr = s[start:end] # O(m)
        if len(substr) != (end - start): # found duplicates or EOS
            break
        if sorted(substr) == list(substr):
            maxsubstr = substr
print "Longest substring in alphabetical order is: %s" %maxsubstr
