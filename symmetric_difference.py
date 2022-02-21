#work w sets; given 2 sets of integers, M and N, print their symmetric differences
#in asc order one per lie; that is values that exist in either M or N 
# but not in both
#use stdinput and output; call from main

def symm_diff(list1, list2): #completed
    dif1 = set(list1).difference(set(list2)) #values that exist in set1 but not set2
    dif2 = set(list2).difference(set(list1))
    union = set.union(dif1, dif2) #combine the 2 sets
    to_list = list(union) #back to a list so can sort(sets are unordered)
    res = sorted(to_list)
    for r in res:
        print(r)

#used for quicker testing
#symm_diff([2, 4,5,9],  [2,4,11,12]) #one int per line -> 5 9 11 12


if __name__ == '__main__':
    N = input() #for ex 4
    n = input() #input  '2 4 5 9'
    lis = n.split()
    #make the space separated list into a list of integers
    list1 = list(map(int,lis)) 

    M = input()
    m = input()
    lis2 = m.split()
    list2 = list(map(int, lis2))
    symm_diff(list1, list2) #calling method on data entered in terminal


    