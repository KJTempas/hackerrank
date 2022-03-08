def captain(k, rooms):
    from collections import Counter
    from operator import itemgetter

    c = Counter(rooms)
    #get key of min value in counter
    min_key = min(c.items(), key=itemgetter(1))
    return min_key[0]
    #this works too
    #print(c.most_common()[-1][0])

# captain(5, [1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2]) #8
# captain(3, [1,1,1,2,2,2,3,3,3,4]) #4

if __name__ == '__main__':
    k = int(input())
    rooms = list(map(int, input().strip().split()))
    print(captain(k, rooms))