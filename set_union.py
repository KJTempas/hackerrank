# a = students who get English newspaper
# b = students who get French newspaper
# goal - determine total number of student who have at least one subscription

def union_sets(a,b):
    print(len(a.union(b)))

#union_sets({1,2,3,4,5,6,7,8,9}, {10,1,2,3,11,21,55,6,8}) #13

if __name__ == '__main__':
    n = int(input())
    # not using n and b to limit size of a and b -> comment to this effect in discussion
    a = set(map(int, input().strip().split()))
    b = int(input())
    b = set(map(int, input().strip().split()))
    union_sets(a, b)