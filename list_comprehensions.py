

def list_comprehensions(x,y,z,n):
    options = [[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1)] 
    result = [x for x in options if sum(x)!=n]
    print(result)


#list_comprehensions(1,1,1,2) # 
#[0,0,0], [0,0,1], [0,1,0], [1,0,0],[1,1,1] #5 lists; not {1,1,0 etc}
#list_comprehensions(2,2,2,2) # There are lots of them

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    list_comprehensions(x,y,z,n)

#in the terminal type in the x y z and n values, then the function runs