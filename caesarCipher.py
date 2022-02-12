#rotate letter in string s by k; ex if k = 3 a -> d and l->0
#wrap end of alphabet, so w,x,y,z map to z,a,b,c if k=3
#cipher only encrpyts letters; symbols, such as - remain unencrypted
# always positive
def caesarCipher(s, k): #correct
    results = ""
    if k>26: #if k greater than alphabet length; 
        k = k%26
    for l in s: #loop through the string
        #ord() return integer representing the unicode char
        #chr() return char(string) from an integer (unicode) of char)
        if l.isalpha(): #so ignore -,.etc
            x = ord(l) #decimal unicode Latin
            x = x+k # apply k 
            if l.isupper() and x>90: #deal with wrap z to a
                x = x-26
            elif l.islower() and x>122:
                x = x-26
            #find char at this new unicode and add to results string
            y = chr(x)
            results = results + y
        else: #if not alpha, no change, just add to results string
            results = results + l
    return results

caesarCipher("There's-a-starman-waiting-in-the-sky", 3) #Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb"
caesarCipher("middle-Outz", 2) # okffng-Qwvb
caesarCipher("AZaz",2) #CBcb
print(caesarCipher("abyzABYZ", 28))
