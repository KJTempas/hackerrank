
#def dynamicArray(n, queries): 
    #lastAnswer =0
   #create empty 2d array of length n
   #https://stackoverflow.com/questions/24023115/how-to-initialise-a-2d-array-in-python
    #this passes pretest, but gets runtime error in rest of test
    # arr = [[] for i in range(n)]
    # answersArr =[]
    # for q in queries: 
    #     if q[0] ==1:
    #         idx = ((q[1] ^ lastAnswer) %n ) #formulas give in challenge
    #         if idx == 0:
    #             arr[0].append(q[2])
    #         else:
    #             arr[1].append(q[2])
    #     else:
    #         idx = ((q[1] ^ lastAnswer) % n )
    #         lastAnswer = arr[idx][q[2] % len(arr[idx])]
    #         answersArr.append(lastAnswer) 
    # return answersArr

    #answer from another - modified mine; it is slighly simpler
#     lastAnswer =0
#     arr = [[] for i in range(n)]
#     answersArr =[]
#     for q in queries: 
#         x = q[1]
#         y = q[2]
#         if q[0] ==1:
#             idx = ((x ^ lastAnswer) %n ) #formulas given in challenge
#             arr[idx].append(y)
#         elif q[0] == 2:
#             idx = ((x ^ lastAnswer) % n )
#             lastAnswer = arr[idx][y % len(arr[idx])]
#             answersArr.append(lastAnswer) 
#     return answersArr

# print(dynamicArray(2, [[1,0,5], [1,1,7], [1,0,3], [2,1,0], [2,1,1]])) # [7 3]



