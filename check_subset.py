#given 2 sets, A and B, find whether A is a subset opf B
#if so , print True else print False

def subset(A,B):
    print(True if set(A).issubset(set(B)) else False)


# subset({1,2,3,5,6}, {9,8,5,6,3,2,1,4,7}) #True
# subset({2}, {3,6,5,4,1}) #False
# subset({1,2,3,5,6,8,9}, {9,8,2}) # False

#input from STDIN
if __name__ == '__main__':
    t = int(input()) #number of test cases
    for i in range(t):
        a = int(input()) #number of elements in A
        A = list(map(int,input().strip().split()))
        b = int(input()) #number of elements in B
        B = list(map(int,input().strip().split()))

        subset(A,B)
