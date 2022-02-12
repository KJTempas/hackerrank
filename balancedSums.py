#AKA #sherlock and array
#find an alement of the array such that the sum of all elements to the L = 
#sum of all elements to the R
#def balancedSums(arr):  
    #this works if don't move elements in array, but does not pass tests
    # through looking at discussion, I see that arr can be rearranged
    # for i in range(1,len(arr)-1):
    #     a = arr[0:i] #index 0 to i
    #     b = arr[i+1:] #index i+1 to the end; leave middle number
    #     if sum(a) == sum(b):
    #         return 'YES'
    # return 'NO'
    #solutions where array can be rearranged
    #good sulution
    # total = sum(arr)
    # add = 0
    # for el in arr:
    #     if add == total - el - add:     
    #         return "YES"
    #     add += el
    # return "NO"


#print(balancedSums([5,6,8,11])) #YES
# print(balancedSums([1,2,3])) #NO
# print(balancedSums([1,2,3,3])) #YES
# print(balancedSums([1,2,3,5,5,1,0])) #yes
# print(balancedSums([1,1,4,1,1] )) #YES
# print(balancedSums([2,0,0,0])) #YES ? 
# print(balancedSums([ 0,0,2,0])) #YES ?
