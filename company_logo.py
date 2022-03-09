#find 3 most common characters  and occurrentce coutn in string; 
#sort output in desc order; sort char in alpha order if count is same


def logo(s):
    from collections import Counter
    #sort string, then send to counter
    # show only top 3 most common letters
    x = Counter(sorted(s)).most_common(3) #x is a list of tuples
    #print each element in x on a separate line
    #help from here on converting tuple of string/int to string
    https://codefather.tech/blog/tuple-to-string-python/#:~:text=The%20simplest%20method%20to%20convert,by%20using%20the%20map%20function.
    for i in x:
        delimiter = ' ' #space between two data pieces in tuple
        y = delimiter.join([str(value) for value in i])
        print(y)
    #this doesn't work for me
    #[print(*x) for x in Counter(sorted(s)).most_common(3)]
    


# logo('GOOGLEXYZ')
# #G 2
# #O 2
# #E 1
# logo('aabbbccde') # b 3 a 2 c 2 on separate lines
# logo('ccaabbbde') # b 3 a 2 c 2

if __name__ == '__main__':
    s = input()
    logo(s)

    #alt answer - not sure it works - gives invalid syntax erroe
    # from collections import Counter, OrderedDict #OrderedDict class not needed?

    # class OrderedCounter(Counter, OrderedDict):
    #     pass
    # [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
#the *c is for unpacking variables, so (1, 2) will become 1 2, and [1,2,3] will become 1 2 3
#then don't need my elaborate method above