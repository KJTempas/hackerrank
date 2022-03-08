from itertools import product

#itertools prod yields combinations of two lists - like nested for loops

def prod(A, B):
    #return product(A,B) #this returns an interator product object
    #ouput from next line  is tuples with , between; don't want ,
    #return tuple(product(A,B))
 
    print(' '.join(str(x) for x in tuple(product(A,B))))


#prod([1, 2], [3, 4]) #(1,3) (1,4) (2,3) (2,4)

if __name__=='__main__':
   
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    prod(A,B)
  