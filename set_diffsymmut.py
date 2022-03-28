#goal find total number of students wo have subscribed to only English newspaper
#some get both) -so need total Engl - (Engl + French)
def set_diff(A,B):
    A = set(A)
    B = set(B)
    #print(A.difference(B)
    print(A-B)
    print(len(A-B))

def sym_diff(A,B):
    #.symmetric_difference() operator returns a set w all the elemends that are
    #in the set and the iterable but not both (not intersection)
    #alt is a ^ operator but operatoes on the set of the elemens in set
    A= set(A)
    B = set(B)
    print(A^B)
    print(len(A^B))


#set_diff([1,2,3,4,5,6,7,8,9], [10,1,2,3,11,21,55,6,8]) #4
#sym_diff([1,2,3,4,5,6,7,8,9], [10,1,2,3,11,21,55,6,8]) #8


# if __name__ == "__main__":
#     n = int(input()) # number of students in A
#     #A =students who get English newspaper
#     A = list(map(int, input().strip().split()))
#     m = int(input())
#     #B -students who get French newspaper
#     B = list(map(int, input().strip().split()))

#     set_diff(A,B)
#     sym_diff(A,B)
#alt input an ssolution to sym
# n1 = int(input())
# e = set(input().split())

# n2 = int(input())
# f = set(input().split())

# result = e.union(f) - e.intersection(f)
# print(len(result))

#-------------
#set mutation options
#.update() or |= means update the set by addig elements from an iterabe/another set
#.intersection_update() or &= means update the set by keeping only elements found in it and an iterable/another set
#.difference_update() or -= means update set by removing elements found in an interable/another set
#.symmetric_difference_update() or ^= means update set by only keeping the elements found in either set, but not in both

def set_mut(A,B):
    



#test data for mutations - result should be 38
#  16
#  1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
#  4
#  intersection_update 10
#  2 3 5 6 8 9 1 4 7 11
#  update 2
#  55 66
#  symmetric_difference_update 5
#  22 7 35 62 58
#  difference_update 7
#  11 22 35 55 58 62 66