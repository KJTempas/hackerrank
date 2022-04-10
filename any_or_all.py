    #any_or_all - completed
    #goal - return  true if all input numbers are positive and 
    #at least one number is a palindrome(reversible)
    #all() returns true if all elements in an iterable are true; else false
    #any() returns true if any element in  an iterable is true
if __name__ == '__main__':
    n = int(input())
    x = list(map(int,input().strip().split()))
    print((all(i>0 for i in x)) and any(str(i) == str(i)[::-1] for i in x))
        
    #another way to do  imput
#N,n = int(raw_input()),raw_input().split()
#don't need map list because raw_input.split()  already  creates a list
