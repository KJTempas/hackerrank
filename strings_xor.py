#find the XOR of the two strings
def strings_xor(s,t): #completed
    #original to debug
    # res = ""
    # for i in range(len(s)):
    #     if s[i] = t[i]:
    #         res = '0'
    #     else:
    #         res = '1'
    # return res

#my revision - note - can only modify 3 lines
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]: #make ==
            res =  res + '0' #change this line
        else:
            res = res + '1' #change this line
    return res

print(strings_xor('10101', '00101') )#10000
