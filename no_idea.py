
#array of integers
# 2 disjoint sets, A and B
#you like all ints in A and don't like those in B
#happiness score 0. loop through array; if i in A happiness +1; if in B happiness -1
#return happiness
 #does not pass all test cases - not sure why- huge test case
def no_idea(arr, A, B):
    #use the in operator for each element in arr
    #if ele is in A +1, if in B -1, so subtract
    arr = set(arr) #needed?
    print(sum([(i in A) - (i in B) for i in arr]))

# no_idea([1,5,3], (3,1),(5,7)) #1
#no_idea([1,2,3,4,5], (4, 2, 1), (4, 6)) #2

 
if __name__ == "__main__":
   # n, m = [int(x) for x in input().split()] #alt method
    n, m = map(int, input().split())
    arr = map(int,input().split())

    a = input()
    A = map(int,a.split())
    b = input()
    B = map(int,b.split())

    no_idea(arr, A, B)

# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, A and B, respectively.