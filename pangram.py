def pangram(s): #completed
    #convert s to all lowercase; 
     #split at space, rejoin with no spaces 
    if s[-1]=='.': #trim off period if there is one
        s = s[0:-1]
    print(s)
    s = ("".join((s.lower()).split()))
    # use collections counter 
    # if len of result =26 -> pangram
    from collections import Counter
    c = Counter(s)
    if len(c) == 26: #every letter of alphabet
        return 'pangram'
    else:
        return 'not pangram'

print(pangram('The quick brown fox jumps over the lazy dog.')) # 'pangram'
print(pangram('The quick brown fox jumps over the lay dog.')) # 'not pangram'
print(pangram('abcdefghijklmnopqrstuvwxyz.')) # pangram
print(pangram('bcdefghijklmnopqrstuvwxyz.') )# not pangram
print(pangram('qmExzBIJmdELxyOFWvLOCmefk TwPhargKSPEqSxzveiun'))#pangram
