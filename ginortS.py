#given a string, sort as follows:
#all sorted lowercase letters are ahead of uppercase letters
#all sorted uppercase letters are ahead of digits
#all sorted odd digits are ahead of sorted even digits

def sorting(s):
    x = [e for e in s] # convert to list
    lower = filter(lambda y: y.islower(), x) #only lowercase after filtering
    upper = filter(lambda y: y.isupper(), x)
    num = filter(lambda y: y.isdigit(), x)
    lower.sort()
    upper.sort()
    nums_even = filter(lambda x: int(x)%2==0, num)
    nums_odd = filter(lambda x: int(x)%2!=0, num)
    nums_even.sort()
    nums_odd.sort()
    print(''.join(lower + upper + nums_odd + nums_even))
    
#sorting('SAorting1234') # ginortAS1324
#below this test case failed - note 0; my answer has 1357924680, forgot to sort numbers
sorting('1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPASDFGHJKLZXCVBNM')
#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468

# if __name__ == '__main__':
#     s = input()
#     sorting(s)

#in hackerrank, this caused a runtimeError with message - 
#AttributeError: 'filter' object has no attribute 'sort'
# I must be on python 2.x  I found in python3 filter returns a filter object, 
#must convert to list by, for ex lower = list(filter(lambda....))
#then it passed