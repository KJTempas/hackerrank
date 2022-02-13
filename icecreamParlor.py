#m = total money to spend
#arr = list of prices of ice cream flavors
#return 1 based index of flavors 2 people can buy that equals m
#answer should be sorted ascending
#they use all of their money

def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == m:
                #+1 to make 1 based index instead of normal 0 based
                return sorted([(i+1), (j+1)])


print(icecreamParlor(6, [1,3,4,5,6])) # [1, 4]
print(icecreamParlor(4, [1,4,5,3,2]) )#1 4
print(icecreamParlor(4, [2,2,4,3])) #1 2
print(icecreamParlor(6, [1, 3, 2, 4])) #3 4

#constraints:
#n<=n<=10000
#there will always be a unique solution