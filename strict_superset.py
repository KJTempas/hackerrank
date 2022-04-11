#strict superset 
#issuperset() returns True if a set has every element of another
#set(passed as arg)
if __name__ == '__main__':
    A = set(map(int, input().strip().split()))
    n = int(input())
    all_n_sets = []
    for _ in range(n):
        x = set(map(int, input().strip().split()))
        all_n_sets.append(x)
    print(all(A.issuperset(x) for x in all_n_sets))
#alt solution
# seta = set(map(input().split()))
# print(all([seta.issuperset(set(map(int, input().split()))) for i in range(int(input()))]))