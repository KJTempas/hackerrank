# can youpermutate the arrays so that A[i] + B[i]>=k for all instances
# if so - return yes, otherwise no

def twoArrays(k, A, B): 
    hold 2nd array constant; find all arrangements of A and test summation
    from itertools import permutations
    perms = list(permutations(A)) #all possible combos of array A
    l = len(A)
    i=0
    for p in perms:
        counter = 0
        for i in range(l):
    #loop through each perm of A and add with B elements
            x = p[i] + B[i]
            if x >= k:
                counter += 1
                i += 1
            else:
                i += 1
        if counter == l:
            return 'YES'
     return 'NO'
    this code works for me and pretest works, but when I submit code, it
terminates due to timeout - did not execute within time limits;
need to optimize code

        planB
        sort the two arrays, one asc and the other desc
    A.sort()  #this solution worked; took less time
    B.sort(reverse=True)
    #add min of one array with max of the other
    for i in range(len(A)):
        if(A[i] + B[i] <k):
            return 'NO'
    return 'YES'
       
print(twoArrays(1, [0,1], [0,2])) #"YES" because if you rearrange A to [1,0] 
#then 1+0>=1 and 0+2>=1
print(twoArrays(10, [2,1,3],[7,8,9])) # YES 1+9, 2+8, 3+7
print(twoArrays(5, [1,2,2,1], [3,3,3,4])) #NO
