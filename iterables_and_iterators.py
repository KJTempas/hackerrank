#how many tupes of length k contain the contain the letter 'a''
#use 1 based indexing
import itertools
from itertools import combinations


def iter(list1, k):
    #get all combos of list1 w no repeats
    # x =itertools.combinations(list1, k) #works
    # print(list(x)) #returns  list of tuples
    # print(type(list(x)))
    # print(len(list(x))) #WHY???
    
    def is_valid(data):
        if 'a' in data:
            return True

    x = filter(is_valid, itertools.combinations(list1, k))
    print(x)  #this gives me 5 answers, which is correct
    print(len(x)) #5, also correct
    lenx = len(x)
    print(lenx) #5
    #total # of combos from itertools.combinations
    y = itertools.combinations(list1, k)
    print(len(list(y))) #6
    leny = len(list(y)) #0?????
    print(leny)
    

iter(['a','a','c','d'], 2)

#helpful info
#https://stackoverflow.com/questions/36211680/2n-itertools-combinations-with-advanced-filtering