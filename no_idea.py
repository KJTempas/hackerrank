
#array of integers
# 2 disjoint sets, A and B
#you like all ints in A and don't like those in B
#happiness score 0. loop through array; if i in A happiness +1; if in B happiness -1
#return happiness
 #??? why A and B not a and b ?

 #this works locally and on initial hackerrank test, but fails 5/8 testcases
 #I unlocked one test case and it was enormous; n=100000 and m=14544
 
def no_idea(arr, A, B):
    h = 0
    for i in arr:
        if i in A:
            h += 1
        if i in B:
            h -= 1
    print(h)


# no_idea([1,5,3], (3,1),(5,7)) #1
# no_idea([1,2,3,4,5], (4, 2, 1), (4, 6)) #2

 
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