#piling_up
# There is a horizontal row of  cubes. The length of each cube is 
# given. You need to create a new vertical pile of cubes. 
# The new pile should follow these directions: if cube[i] is on top 
# of cube[j], the side Len of j >=sideLength i  
# When stacking the cubes, you can only pick up either the 
# leftmost or the rightmost cube each time. 
# Print Yes if it is possible to stack the cubes.
#  Otherwise, print No.
#code passed initial test, but not all of full test; 
#Terminated due to timeout; conde needs to be optimized
def piling_up(nums):
    #figure out largest between the 2 sides of list - call it the base
    base = nums.pop(0) if nums[0]>=nums[-1] else nums.pop(-1)
    while len(nums)>1:
        #first determine which is larger 0 or -1
        #then if larger number is <=base, pop it
        #else check if smaller number is <=base; if so  pop it
        if nums[0]>=nums[-1]:
            if nums[0]<=base:
                x = nums.pop(0) #pop returns the popped values
                base=x
            #nums[-1] must be >num[0]
        elif nums[-1]<=base:
            x = nums.pop(-1)
            base = x
        else:
           return 'No'
    if nums[0]<=base:
        return 'Yes'
    else:
        return 'No'
    
      #maybe a way to do this using deque???  
# print(piling_up([1,2,3,8,7])) #No after 7 1 stuck because 2 and 8 are both >1
# print(piling_up([1,2,3,7,8])) #yes - can stack 8 7 3 2 1
# print(piling_up([5, 3, 2, 4, 6])) #yes - 65432
# print(piling_up([5, 3, 2, 8, 4, 6])) # no 6,5,4,3,2 but then 8 >base, so NO

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        nums = list(map(int,input().strip().split()))
        print(piling_up(nums))

        #using deque is must more efficient
#here is a solution using deque
from collections import deque
#collections.deque implements a queue and performs append and pop fx 
#quicker than lists
for _ in range(int(input())):  
    #this handles n and nums is a queue
    _, queue =input(), deque(map(int, input().split()))
    #TODO I don't understnad why sorted,reversed and the == below
    for cube in reversed(sorted(queue)):
        if queue[-1] == cube: queue.pop()
        elif queue[0] == cube: queue.popleft()
        else:
            print('No')
            break
    else: print('Yes')
#explanation of this use of deque
# He first made the deque from the inputs that part is simple.
# After that he sorted the nums in the deque and started reading 
# them in reverse order. Remeber he didn't store the sorted deque 
# anywhere, he is just iterating over it.
# So first he pick the biggest size (because he is reading in 
# reverse order ) and check whether the item on the left side or 
# right side of the deque is equal to that, and if such a number 
# exist he poped it from the deque.
# Finally if he didn't find such number it means the numbers 
# in the deque are in such a order that you can't make the pile.