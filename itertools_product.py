# from itertools import product
# #itertools prod yields combinations of two lists - like nested for loops

# def prod(A, B):
#     #return product(A,B) #this returns an interator product object
#     #ouput from next line  is tuples with , between; don't want ,
#     #return tuple(product(A,B))

#     print(' '.join(str(x) for x in tuple(product(A,B))))
# #prod([1, 2], [3, 4]) #(1,3) (1,4) (2,3) (2,4)

# if __name__=='__main__':
#    #input is 2 lists of space separated numbers
#     A = list(map(int,input().strip().split()))
#     B = list(map(int,input().strip().split()))
#     prod(A,B)
  
  #---------------------
  #itertools combinations

from itertools import combinations
#itertools.combinations(iterable, r) returns the r length 
#subsequences of elements from the input iterable
if __name__=='__main__':
    #input is single line containing string S and integer value k separated by space
    s, k = input().split()
    s = sorted(s)
    k =int(k)

    for i in range(1,k+1):
      #  print(*combinations(s, i), sep = "\n") #this prints as tuples
        for c in combinations(s, i):
            print(''.join(c)) #join parts of the tuple without the comma


#goal for input HACK 2 is 
#A
#C
#H
#K
#AC
#AH
#etc