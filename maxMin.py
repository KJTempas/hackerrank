#goal given arr and integer k, create an array of length k from elements in arr
#such that its unfairness is minimized; 
#unfairness = max(arr') - min(arr')
def maxMin(k, arr):
# find all combos of length k  (no repeats); for each one determine max-min; 
# store 1st value ; if next max-min is less, replace;
# return min possible unfairness
# this answer works in pretest, but causes a runtime error: takes too long
# need to simplify???
    from itertools import combinations
    combo = combinations(arr, k) #all combos of arr of length k that are unique
    min_fairness = max(arr)#set min as largest number 
    for i in list(combo):
        print(i)
        x = abs(max(i) - min(i))    
        if x<min_fairness: #replace min_fairness with x
            min_fairness = x  
    return min_fairness
   
   #THIS METHOD TAKES LESS CALCULATIONS - more efficient, and works
    # arr.sort()
    # n = len(arr)
    # min_dif = max(arr) #set for comparison
    # for i in range((n-k)+1):
    #     dif = arr[i+(k-1)] - arr[i]
    #     if dif<min_dif:
    #         min_dif = dif
    # return min_dif
    
maxMin(2, [1,4,7,2]) #[1,2] is minimum possible unfairness, which is 1
maxMin(4, [1,2,3,4,10,20,30,40,100,200]) #3
