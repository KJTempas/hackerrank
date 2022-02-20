#use itertools.groupby
# The operation of groupby() is similar to the uniq filter in Unix. 
# It generates a break or new group every time the value of the key 
# function changes 
#in other words, it only groups the items if their key- result is the same for successive items
import itertools
from itertools import groupby

def compress_the_string(s): #completed  (level Medium)
    res = ''
    #change string to list
    l = [ char for char in s]
    #see notes above; key is number, group is how many of the key there are in succession
    for key, group in groupby(l):
      #return needs to be one line with space between each tuple(which must be converted to a string)
       res = res + str(((len(list(group)), int(key)))) + ' '
    return res.rstrip()


#compress_the_string('1222311')
#(1, 1) (3, 2) (1, 3) (2, 1) #all on one line

#more info at https://stackoverflow.com/questions/41411492/what-is-itertools-groupby-used-for


if __name__ == '__main__':
    s = input()

    print(compress_the_string(s))