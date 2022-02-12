#wk 2 Hackerrank
#array of integers representing the color of each sock
#determine how many pairs of socks w matching colors there are
def sockMerchant(n, ar):
    from collections import Counter
    c = Counter(ar) #counter is like a dictionary
    tally=0
    for x in c.values():
        tally += x//2
    return tally

sockMerchant(7, [1,2,1,2,1,3,2]) #2
sockMerchant(9, [10,20,20,10,10,30,50,10,20]) #3
