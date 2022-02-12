#Louise and Richard have a numbers game. They pick and number and check to 
#see if it is a power of 2.  If yes, they divide it by 2, if not, they reduce it by
#the next lower number which is a power of 2. Whoever reduces the number to 1 wins the game. 
#Louise always goes first
#start at initial value n
def counterGame(n):
    import math
    #TODO NOT DONE YET - passed initial test; failed many other tests, then timedout
    # look at https://stackoverflow.com/questions/50012693/how-to-switch-between-players-in-tic-tac-toe-in-python
    turn =0
    players = ['Louise', 'Richard']
    player = players[turn]
    while n>1:
        #if n is a power of 2, divide n by 2
        bin_n = bin(n)
        list1=list(bin_n)[2:]
        print('l', list1)
        if list1.count('1') == 1: #powers of 2 are 1000000 like numbers; 1x1 and many 0s
            n = int(n/2)
            print('you are here', n) #8.0  a float
        else: #else find highest power of two less than n and , and do n - that number = new n
            result = highestPowerOf2(n)
            print('r',result)
            n = n - result
            print('n', n)
        if n>1:
            turn +=1
            print('t1',turn)
    print('t2',turn)
    p = turn%2
    print('3',p)
    print('4', players[p])
    return players[p]

        
def highestPowerOf2(n):
    result = 0
    for i in range(n, 0, -1): #step backwards from n
        if ((i & (i-1)) == 0):
            # if 10 &bitwise AND 9 ==0; if 9 &8 ==0
            result = i
            break
    return result
#alt solution
def counterGame(n):
    if n == 1:
        return "Richard"
    
    counter = 1
    while n != 1:
        log_n = math.log2(n)
        if log_n.is_integer():
            n = int(n / 2)
        else:
            n = n - math.pow(2, int(log_n))
        counter += 1
    
    if counter % 2 == 0:
        return "Louise"
    else:
        return "Richard"

#another solution
def counterGame(n):
    i = 1
    while n > 1 :
        i += 1; k = 0
        while 2 ** k < n : k += 1
        n = n / 2 if 2 ** k == n else n - 2 ** (k-1)
    return "Louise" if i % 2 == 0 else "Richard" 

#3rd alt solution
import math
def counterGame(n):

    count = 1
   
    if n <= 1:
        print("Richard")
    
    while n >= 1:
        m = 0
        ans = int(math.log(n, 2))
        if 2**(ans)==n:
            count += 1
            n = int(n/2)
        else:
            count += 1
            m = 1 << int(math.log(n) // math.log(2))
            n -= m

    return ("Richard")if count % 2 == 0 else ("Louise")

# #https://www.geeksforgeeks.org/highest-power-2-less-equal-given-number/
# counterGame(16) #Richard-L passes 8 to R; R passes 4 to L; L passes 2 to R; R take 2 to 1 and  R wins
# counterGame(6) #*'Richard' L passes 2 to R;  R reduces 2 to 1 and wins
# counterGame(132)#  'Richard' *?
# counterGame(5) #'Louise - L passes 1 to R
