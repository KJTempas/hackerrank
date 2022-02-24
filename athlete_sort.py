# You are given a spreadsheet that contains a list of  athletes 
# and their details (such as age, height, weight and so on).
#  You are required to sort the data based on the th attribute 
#  and print the final resulting table. 
# Note that  k is indexed from 0 to M-1, where M is the number of attributes.

# Note: If two attributes are the same for different rows, for example, 
# if two atheletes are of the same age, print the row that appeared 
# first in the input.
# #INPUT 
# first line is N # %% [markdown]
# next N lines each contain M elements
# last line is k
#ex  of input
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1
# resulting output - sorted by column of second attribute
# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12

def athlete_sort(arr, k):
    print(arr)
    #sort by k-th element in each subarray


athlete_sort([[10,2,5],[7,1,0],[9,9,9],[1,23,12],[6,5,9]], 1)


#stdinput provided
# if __name__ == '__main__':
#     nm = input().split()
#     n = int(nm[0])
#     m = int(nm[1])
#     arr = []
#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))
#     k = int(input())