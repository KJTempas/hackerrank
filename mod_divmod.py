
from __future__ import division #needed in python2
def mod_divmod(a,b):
    print(a//b)
    print(a%b)
    print(divmod(a,b))


#mod_divmod(117,10) #(17,7)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    mod_divmod(a,b)