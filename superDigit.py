#once again, this works for 2 test cases and pretest, but not in submit code tests
#it timesout - so there must be a simpler way
# def superDigit(n, k):
#     m = int(str(n) * k)
#     l = len(str(m))
#     while l>1:
#         #make m into a list then can sum it
#         x = [int(y) for y in str(m)]
#         s = sum(x)
#         l = len(str(s))
#         m = s
#     return m     
#from discussion - if you have time exec problems 
# def superDigit(n, k): # Write your code here 
#   if (k % 10 != 0): n = str(n) * k while(int(n) > 10): digit = 0 for number in str(n): digit += int(number) n = digit return(n)
#another discusssion - says multiply the sum of digits in n by k instead of multiplyint the string n by k directly
#this would take less time and prevents a run time error
def superDigit(n, k):
    if len(str(n)) < 2:  #doesn't work either; confused about timeout
        return n
    num = sum([int(digit) for digit in n]) * k
    return superDigit(str(num), 1)


#superDigit(9875,1) #2 because 9+8+7+5 = 29 and 2 + 9 = 11 and 1 + 1 = 2
#superDigit(9875, 4)# 8 because 9+8+9+5 + ... = 116 and 1+1+6 = 8
#stop when one digit