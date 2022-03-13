# Some basic hackerrank challenges are in this file.
# I felt they didn't need their own individual file



#https://www.linode.com/docs/api/linode-types/#type-view - 
#test extracting specific results from a json api response and using them to calculate
# cost
#Hackerrank

#---------
#m = month d = date of birthday 
#Hackerrank
# def birthdays(s,d,m):
#     if len(s)==1:
#         if d == s[0]:
#             return 1
#         else:
#             return 0
#     else: #s is a list of length >1
#     #subgroups have to be successive numbers of length m
#         all_combos = []
#         i=0
#         for i in range(len(s)-(m-1)):
#             new_arr= s[i:i+m]
#         #loop through all combos and find number of combos that sum to d
#             all_combos.append(new_arr)
#             new_arr =[]
#         counter = 0
#         for a in all_combos:
#             if sum(a) == d:
#                 counter +=1
#         return counter

# print(birthdays([2,2,1,3,2], 4, 2)) #2 
# print(birthdays([3,3,1,3,2], 6, 2)) #1
# print(birthdays([3,3,1,3,1], 4, 2)) #3
# print(birthdays([4], 4,1)) #1
# print(birthdays([2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1], 18, 7)) #3

#-----------------
#Monthly challenge #
#1 Find the median - middle number 
# def findMedian(arr):
#     s = sorted(arr)
#     return s[len(arr)//2]

# findMedian([5,3,1,2,4]) #3
# findMedian([0,1,2,4,6,5,3]) #3
# findMedian([1,3,5,7,9]) #5

#-----------------
#2 Flipping the matrix
#If it helps: Don't think about flipping the rows and columns... 
# There are too many possible outcomes.

#Instead, think about what values you can get into the different 
# places. For example, in (0,0) you can get any of the 4 corners. 
# Keep that pattern going and you should start to see a pretty 
# simple algorithm present itself.
#for every m[i][j] from the top left quarter
#m[i][j]  compare to m[i][(2n-1)-j] compare to m[(2n-1)-i][j] compare to m[(2n-1)-i][(2n-1)-j]
#find the max of these values and add to sum
# def flippingMatrix(matrix): #TODO test this with a 6x6 (this is a 4x4)
#     x = len(matrix) # so need top left 2x2
#    #currently works with this 4x4 grid
#     #find max of four corners values and sum them
#     #four corners would be [0,0], [0,x-1], [x-1,0], [x-1, x-1] #row,column
#     max1 = max([matrix[0][0], matrix[0][x-1],matrix[x-1][0], matrix[x-1][x-1]])
#     max2 = max([matrix[0][1], matrix[0][x-2],matrix[x-1][1], matrix[x-1][x-2]])
#     max3 = max([matrix[1][0], matrix[1][x-1],matrix[x-2][x-1], matrix[x-2][0]])
#     max4 = max([matrix[1][1], matrix[1][x-2],matrix[x-2][x-2], matrix[x-2][1]])
#     return  max1 + max2 + max3 + max4
 

#print(flippingMatrix([[112,42,83,119],[56,125,56,49],[15,78,101,43],[62,98,114,108]]) )#414


#-------------

#n = number of towers
#m = height of each tower at beginning
#goal - each turn a player choose a tower of ht x and reduce 
#its height to y where y evenly divides x; if unable to move
#you lose gem; if P1 wins, rturn 1; else 2
# [def towerBreakers(n,m): #TODO solve this
#     #p = 1 #player 1; after move, change to p=2; after move change back to p=1
#     players = [1,2]
#     #while true?
#     tower_heights = []
#     for i in range(n):
#        # print(i+1)  #tower 1 and tower 2
#         tower_heights.append(m) #height of each tower at beginning
#     print(tower_heights)
#     for p in players:
#         #start w tallest tower?
#         tallest = max(tower_heights)
#         print(tallest)
#         to_1 = tallest - (tallest-1)
#         print(to_1)
#         if tallest%to_1 ==0:
#             print('hi')
#             new_h]t = tallest - (tallest -(tallest-1))


#towerBreakers(2,2)# 2
#towerBreakers(1,4) #1
#---------------

#--------------------
#
#-----------------------------
#XOR bitwise operator
 #= ^ = x^y; XOR returns 1 if one of the bits is 1 and ther other is 0 else returns false
 #first convert int to binary; https://www.geeksforgeeks.org/python-bitwise-operators/
 #ex a = 10 b = 4; a ^ b = 14

#--------
#if_else - completed
#given an int, n, do this
#if n is odd, print Weird
#if n is even and in inclusive range 2-5, print'Not Weird'
#if n is even and in incl range 6-20, print'Weird'
#if n is even and >20, print'Not Weird

# def if_else(n):
#     if n % 2==0 :  #even
#         return'Weird' if 6<=n<=20 else 'Not Weird'
#     else: #odd
    #    return'Weird'

# print(if_else(8))# Weird
# print(if_else(18)) # Weird
# print(if_else(28)) #Not Weird
# print(if_else(6)) #Weird
# print(if_else(20)) # weird
# print(if_else(3)) #Weird

#if calling from main, this is the setup
# if __name__ == '__main__':

#     n = input()
#     result = if_else(n)
#     print(result)

    #in the termina, type python hackerrank.py(the file name), then 
    #thern enter some input (ie 5) and the result will print
#-----------------

def python_lists(arr):
    pass



if __name__ == '__main__':
    N = int(input()) # number of commands
