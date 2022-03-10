import numpy

def min_max(arr):
    my_array = numpy.array(arr)
    #for numpy.min
    #axis=0 means overall min for each subarray, so for position 1 the min, for position 2, the min
    #axis=1 means look at all values in each subarray and select min 
    #axis=None means look at all values all together and find the overall smallest number
    print(numpy.min(my_array, axis=1))
    print(numpy.max(numpy.min(my_array, axis=1), axis=0))

#min_max([[2,5],[3,7],[1,3],[4,0]]) #3 because the numpy.min is [2, 3, 1, 0] and the max of those numbers is 3

if __name__=='__main__':
    
    n,m = input().split()
    n = int(n)
    m = int(m)
    arr = []

    for i in range(n):
        x = list(map(int,input().strip().split()))
        arr.append(x) #append the subarray to the larger array
    min_max(arr)

#alt answer
print(np.max(np.min(np.array([input().split() for _ in range(int(input().split()[0]))],int),axis=1)))

#alt answer
import numpy as np
n, m = list(map(int, (input().split())))
a = np.array([list(map(int,(input().split()))) for i in range(int(n))])
print(np.max(np.min(a, axis = 1), axis = None))