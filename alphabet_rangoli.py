
#def rangoli(n):
    #use string center(); string.center(length, character)
    #alpha = '0abcdefghijklmnopqrstuvwxyz'
    #print(alpha[3]) #c
    # x = (2*n)-1 #how many rows #5 for n=3
    # y = n*n #how many in a row #9
    # for i in range(x):
    #     print(alpha[2].center(x, '-'))
    
    # for i in range(1, x):
        #need to center letters, and center letters in larger grid
       # print(alpha[n].center(y, '-'))

       # print((alpha[n] +'-' +  alpha[n-1] + '-' + alpha[n]).center(y,'-'))
    #try making a string with letters needed and then '_'.join(s))
    #https://www.pythonprogramming.in/efficient-way-to-add-spaces-between-characters-in-a-string-in-python.html
        
    #
    # 1st row = alpha[n] centered
    # 2nd row = alpha[n]+ alpha[n-1] + alpha[n] centered , and that centered with '-'
    # 3rd row = alpha[n] + alpha[n-1] + alpha [n-2]
    #so need nested loops
    #middle centered element takes up 1,5,9, 13
#rangoli(3)
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

#how many lines is answer? if 3-> 5; if 5 -> 9; if 10 -> 19; so 2n-1

#this from designer_doormat.py
#syntax is string.center(length, (opt)charater to fill missing spaces(default is " "))
# N, M = map(int,input().split())
# for i in range(1,N,2): 
#     print((i * ".|.").center(M, "-"))
# print("WELCOME".center(M,"-"))
# for i in range(N-2,-1,-2): 
#     print((i * ".|.").center(M, "-")

#https://www.journaldev.com/23788/python-string-module#
import string #string module  includes ascii_lowercase, which is abcd....
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    #making each line
    s = "-".join(alpha[i:n])
    #to the list, append s in reverse order + s forward order centered in 4n-3 spaces, separated by '-'
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))

