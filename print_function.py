

def print_funct(n):
    res = ''
    for i in range(1,n+1):
        res +=str(i)
    print(res)

# print_funct(3) # '123'
# print_funct(12) # '123456789101112'


if __name__ == '__main__':
   n = int(input())
   print_funct(n)
   
