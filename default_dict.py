 #you are given 2 integers, n and m; there are n words, which might repeat,
# in word groupA. There are m words belonging to group B. For each m words, check
# whether the word has appeared in group A or not.  
# Print the indices of each occurrence of m in group A.  
# If it does not appear, print -1
from collections import defaultdict

if __name__ == '__main__':
    #alt way to input
    #n,m = map(int, raw_input().split()) #raw_input doesn't work for me
    n,m = map(int, input().split())
    n = int(n)
    m = int(m)
    d = defaultdict(list)
    for _ in range(n):
        d['groupA'].append(input())
    for _ in range(m):
        d['groupB'].append(input())
#actually only need groupA to be default dict; B can just be a list
    for x in d['groupB']:     #loop through values in B
        indexes = [i for i, j in enumerate(d['groupA']) if j == x]
        indexes =[i+1 for i in indexes]
        if indexes:
            print(*indexes, sep=' ') #use * to unpack a list
        else:
            print(-1)
#alt - for i in groupB(a list)
   # if i in d (default dict):
      #  print(" ".join(map(str, d[i])
      #else:
      #print(-1)
#default_dict(['a', 'b', 'a'], ['a','c']) #result is 1 3    -1
#because the first letter in B appears in positions 1 and 3 in A, and 
#the second letter'c' does not appear in A, so  print -1
#use 1 indexed positions
#default_dict(['a','a','b','a','b'],['a','b'])  #1 2 4     next line 3 5


