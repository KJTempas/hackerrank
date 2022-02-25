 #you are given 2 integers, n and m; there are n words, which might repeat,
# in word groupA. There are m words belonging to group B. For each m words, check
# whether the word has appeared in group A or not.  
# Print the indices of each occurrence of m in group A.  
# If it does not appear, print -1

def default_dict(arrA, arrB):
    for t in arrB:
        #enumerate fx takes a collection(tuple, arr) and returns an enum object with a counter as the key of the obj

        indices = [ i for i, x in enumerate(arrA) if x == t]
        if indices:
            print([i+1 for i in indices])
             #TODO output nees to be 2 indices separated by a space, like 1 3   
        else:
            print(-1)
   
    
 



default_dict(['a', 'b', 'a'], ['a','c']) #result is 1 3    -1
#because the first letter in B appears in positions 1 and 3 in A, and 
#the second letter'c' does not appear in A, so  print -1
#use 1 indexed positions
#default_dict(['a','a','b','a','b'],['a','b'])  #1 2 4     next line 3 5



# if __name__ == '__main__':
#     N = int(input())
#     M = int(input())
#     print(N, M)
#     arrA = list(map(int,input().split()))
#     arrB = list(map(int,input().split()))
#     #TODO figure out input - split...
#     #arrA = int(input() i for N i)


