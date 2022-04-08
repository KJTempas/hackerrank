#goal - given n words, for each word, output its number of occurrences
#return output in order of input
#need to use an ordered dictionary to maintain order of accition of elements to dict
import collections 
def word_order(strings):
    dct = collections.OrderedDict()
    for s in strings:
        if s in dct:
            dct[s] = 1 + dct[s] 
        else :
            dct[s] = 1
    values = dct.values() # a list of the order dict values
    #to get rid of [] and , convert list to string
    print(len(dct))
    print(" ".join(map(str, values)))

#word_order(["bcdef", "abcdefg", "bcde", "bcdef"])  #2 1 1
#word_order(['cat', 'dog', 'ant', 'dog']) # 1 2 1


if __name__ == '__main__':
    n = int(input())
    strings = []
    for _ in range(n):
        s = input()
        strings.append(s)
    word_order(strings)

