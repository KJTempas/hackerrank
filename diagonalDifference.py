
def diagonalDifference(arr): #completed
    l =len(arr)
    sum_1=0
    for i in range(l):
        sum_1 = sum_1 +  arr[i][i] # 0,0 + 1,1 + 2,2 +
 #reverse each subarray
    rev_arr = []
    for a in arr:
        a.reverse()
        rev_arr.append(a)
    sum_2=0
    for i in range(l):
        sum_2 = sum_2 + rev_arr[i][i]
    return abs(sum_1 - sum_2)
    

diagonalDifference([[11,3,5],[4,5,6],[10,8,-12]]) #16
diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]]) #15
diagonalDifference([[1,2,3,4],[4,5,6,7],[6,7,8,9],[1,2,3,4]]) #0
