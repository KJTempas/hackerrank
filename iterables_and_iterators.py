#how many tupes of length k contain the contain the letter 'a''
#use 1 based indexing
import itertools
from itertools import combinations
#Very tricky

def iter(list1, k):
    def is_valid(data): #used in filtering list1 below
        if 'a' in data:
            return True

    x = filter(is_valid, itertools.combinations(list1, k))
    lenx = len(x) #this causes an Runtime Error in hackerrank
    #where the message is TypeError: object of type 'filter' has no len()
    #I had to sub this in hackerrank instead of line 13
    # lenx=0
    # for i in x:
    #     lenx+= 1
    #then it passed all tests
    #total # of combos from itertools.combinations
    y = itertools.combinations(list1, k)
    def count_iterable(y): #can't do len on itertools combination object as is
        return sum(1 for e in y)
    leny = count_iterable(y)

    return '{:.3f}'.format(float(lenx)/leny)

#iter(['a','a','c','d'], 2) #0.8333


if __name__== '__main__':
    N = int(input()) # number of elements in list
    def toString(a):
        return str(a)
    list1 = list(map(toString, input().split()))
    k = int(input()) #number of indices to be selected

    print(iter(list1, k))

#helpful info
#https://stackoverflow.com/questions/36211680/2n-itertools-combinations-with-advanced-filtering