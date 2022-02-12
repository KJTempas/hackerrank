#Zig Zag Sequence

#def findZigZagSequence(a, n):
    #need to debug this code 
    #this is original
    # a.sort()
    # mid = int((n + 1)/2)
    # a[mid], a[n-1] = a[n-1], a[mid]

    # st = mid + 1
    # ed = n-1
    # while(st <= ed):
    #     a[st], a[ed] = a[ed], a[st]
    #     st = st + 2
    #     ed = ed +1

    # for i in range (n):
    #     if i == n-1:
    #         print(a[i])
    #     else:
    #         print(a[i], end=' ')
    # return
    

    #my revision - don't understand how it works yet #TODO 
#     a.sort()
#     mid = int((n + 1)/2) #is 3 in test case
#     a[mid], a[n-1] = a[n-1], a[mid]
#     #a[3], a[4] = a[4], a[3]  #switch around? then [1,2,3,4,5] becomes [1,2,3,5,4]

#     st = mid + 1 #st = 4
#     ed = n-1 #ed = 4
#     while(st <= ed):
#         a[st], a[ed] = a[ed], a[st] #a[4], a[4] = a[4], a[4]
#         st = st + 2 #st = 6
#         ed = ed +1 #ed = 5

#     for i in range (n): #range 5
#         if i == n-1: #if i == 4
#             print(a[i])
#         else:
#             print(a[i], end=' ')
#    # return

# findZigZagSequence([2,3,5,1,4], 5) # [1,4,5,3,2]
