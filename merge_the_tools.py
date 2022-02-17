#split string s into length n ; split s into n/k substrings where
#each substring consists of contiguous blocks of k characters in s
#remove repeat chars
#1/17 test cases failed :) but I got a star) - I unlocked test case and it is HUGE
def merge_the_tools(string, k):
  
    for i in range(k):
        sub = string[i*k:(i+1)*k] #make substrings of length k
        x = sorted(set(sub), key=sub.index) #remove dups but maintain order
        s = "".join(x) # back to string
        return s
        
#https://www.codegrepper.com/code-examples/python/remove+duplicates+but+maintain+order+in+a+list+python
#alt method - dictionary from keys()
merge_the_tools('AABCAAADA', 3) #AB CA AD



# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)