#worked for pretest but timed out after half of the tests
#I don't know how to simplify so takes less time
#says subtask - 0<=n<=100 for 60% of the max score

def sumXor(n):
    tally = 0
    for x in range(n+1):
        if n + x == n ^ x:
            tally +=1

    return tally
        
sumXor(4) #4
sumXor(5) #2
print(sumXor(10)) #4
print(sumXor(1000000000000000)) #1073741824 #gives a memory erroron my computer; times out

#an answer
# As bin() returns a binary_string that has '0b' appended in the first 
# two indices, we slice off those first two digits. Since XOR takes the
# of strings with different indices, we count the indices with zeros 
# (since summing values will give you a value greater than the individual 
# parts of the sums; thus the 1's remain inplace). As there are 2 
# choices for each 0 index (i.e. 1,0), we return 2**(# of zeros in string).

# For the case n == 0; since bin(0)[2:].count('0') == 1 and 2^1 = 2 which is incorrect, we need return 1 if n == 0.

# def sumXor(n):
#     #Write your code here
#     return 1 if n == 0 else 2**(bin(n)[2:].count('0'))
#