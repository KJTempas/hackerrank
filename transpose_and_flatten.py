#numpy.transpose creates a copy of the input array flattened to 1 dimension
#given and N X M ingeger array (N rows and M columns)
#task is to transpose and flatten results
#transposed does not affect the original array, but creates a new array

import numpy
def transpose_and_flatten(grid):
    new_arr = numpy.transpose(grid)
    print(new_arr)
    my_array = numpy.array(grid)
    print(my_array.flatten()) #flattens two arrays to be combined into one array no ,



#transpose_and_flatten([1,2,3],[4,5,6]) 
# [[1 4] #transpose
# [2 5]
# [3 6]]
# #flattens to [1 2 3 4 5 6]
#transpose_and_flatten([[1,2],[3,4]])
#[[1 3]  #print transposed array
# [2 4] 
# [1 2 3 4 ] #printflattened array


if __name__ == "__main__":
    row,col = map(int, input().split())
    grid = []
    for i in range(row): #take entry string, split, make ints and make into a list
        entries = list(map(int, input().split())) #then ade that list to the grid []
        grid.append(entries)

    transpose_and_flatten(grid)

#https://www.geeksforgeeks.org/take-matrix-input-from-user-in-python/