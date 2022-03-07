def designer_doormat(n, m):
    i = 1
    y = (m-3)//2
    for r in range(n//2):
        print('-'* (y) + (('.|.') * i) + ('-'* (y)))
        if r<(n//2)-1: #don't add the last time
            i +=2
            y -=3
    mid = (m-7)//2
    print('-' * mid + 'WELCOME' + '-'* mid)
#reverse it
    for t in range(n//2):
        print('-'* (y) + (('.|.') * i) + ('-'* (y)))
        i -=2
        y +=3 

#designer_doormat(7, 21)
#designer_doormat(9,27)

if __name__ == '__main__':
    n,m  = input().split()
    n,m = [int(n), int(m)]
   
    designer_doormat(n,m)

#way more elegant solution using center()
#I didn't know about this string method
#syntax is string.center(length, (opt)charater to fill missing spaces(default is " "))
# N, M = map(int,input().split())
# for i in range(1,N,2): 
#     print((i * ".|.").center(M, "-"))
# print("WELCOME".center(M,"-"))
# for i in range(N-2,-1,-2): 
#     print((i * ".|.").center(M, "-"))
