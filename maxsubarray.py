#subsequences are any subset of an arr; 
#subarray = a contiguous subsequence in an array
#given an array, find the max possible sum among
#1 all nonelmpty subarrays
#2 all nonempty subsequences
#print the 2 values as space separated integers on  one line
#empty subarrays/subsequ should not be considered


# ex - if arr =m [-1,2,3,-4,5,10]
# then max subarray sum is comprised of elements are indices 1-5; sum is 2+3+...+1- = 16
# max subsequ sum, is elements at indices 1,2, 4,5 and sum is 2+3+5+10 = 20

#part of one month prep kit
def maxSubarray(arr):
    #subarr max - contiguous
    #consecutive combinations?
    #elements 1-end, 2-end, 3-end....1-end-1
    max_so_far = min(arr)
    max_ending_here =0
    for i in range(len(arr)):
        max_ending_here = max_ending_here + arr[i] #2 ; 2 = 2+-1 or -1; 
        if(max_so_far < max_ending_here): #if -5 <2; if 2 < -1 no change
            max_so_far = max_ending_here #2
        if(max_ending_here <0): #if 2<0 ; if -1<0, then mEH =0
            max_ending_here = 0
    print(max_so_far)
    return max_so_far
#TODO work this through
        # arr[i]  MEH       MSF
        #at start    0       -5
        # 2           2     2
        # -1       -1       still2
        # 2          1       2
        # 3 
        # 4
        # -5      

#this part works - just commented out while working on top part
    #for subseqence max, sort first, then sum all + numbers; use lambda is positive
    # sa = sorted(arr)
    # print(sa)
    # #sum all positive numbers
    # filtered = filter(lambda s: s>0, sa ) #filter sa so that new list contains only numbers >0
    # print(list(filtered))
    # sum_filtered = sum(list(filtered))
    # print(sum_filtered)

#maxSubarray([1,2,3,4]) # [10  10] 
maxSubarray([2, -1, 2,3,4,-5]) # [10  11]




#TODO input provided, but see if you can figure it out before looking

# if __name__ == '__main __':
#     t = int(input()) #number of test cases #first line is single int t
#     for i in t: #first line of each test is single int n
#         n = int(input()) 
    #second line  contains n space separated ingeters (arr[i])
    #no empty subarrays or subsequ should be considered


#look at  - https://www.geeksforgeeks.org/python-program-for-largest-sum-contiguous-subarray/