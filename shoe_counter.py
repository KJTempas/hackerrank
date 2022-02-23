#calculate amount of money earned by shoe store owner
#input [list of shoe sizes', [(cust show size, cost), etc for a list of  customers]]
#not sure about input of shoesize and cost;  or tuple?
#import sys #to get input from command line

#tricky, especially input; 

def shoe_counter(shoe_sizes,transactions):
    total = 0
    from collections import Counter
    dict = Counter(shoe_sizes)

    for t in transactions:
        #if tuple[0] is a key in x(the dictionary made by counter)
        if t[0] in dict.keys():
            if dict[t[0]]>0: #if the value of that key >0 (number of shoes >0)
                total += t[1] #add the cost(t[1]) to total
                dict[t[0]] -=1 #reduce the value of that dict item by 1 (reduce # of shoes available)
        
    return total

#function works with this input
#shoe_counter([2,3,4,5,6,8,7,6,5,18], [(6,55), (6,45), (6,55), (4,40), (18, 60), (10,50)]) #200

if __name__ == '__main__':
    #input on shoe sizes
    X = input() #number of shoe sizes
    x = input() #indiv shoe sizes entered like this '2 3 4 5 ...'
    # to get shoe sizes into shoe sizes []
    lis = x.split()
    #make the space separated list into a list of integers
    shoe_sizes = list(map(int, lis)) 
    
    #input on transactions of size and cost
   # make tuples size(index[0]) and cost[1]
    transactions = []
    N = input() #number of transactions
    n = int(N)
    line = ''
    for i in range(N): #for each transacion
        line +=input() 
        x = tuple(map(int, line.split()))#split string at space
        transactions.append(x)
        line = '' #clear to make new line for new tuple
  
  #entered in terminal this way
  # 3 #X number of shoes
  # '4 5 6' #shoe sizes
  # 3 #N number of transactions
  # '4 50' #first shoe size and cost
  # '5 55'
  # '6 30'
 

#    #call method
    print(shoe_counter(shoe_sizes, transactions))


##alt input and call strategy in another challenge
    #  s = input()
    # i, c = input().split()
    # s_new = mutate_string(s, int(i), c)
    # print(s_new)


#in hackerrank, get a Runtime error with this 
#   File "/tmp/submission/20220221/21/40/hackerrank-c2046c041f7bd77e5469c211792cc943/code/Solution.py", line 33, in <module>
#     for i in range(N): #for each transacion
# TypeError: 'str' object cannot be interpreted as an integer


    # look at https://stackoverflow.com/questions/19202893/converting-input-from-stdin-into-lists
    #also look at symmetric_difference.py in this folder
    #https://stackoverflow.com/questions/2233917/how-to-input-an-integer-tuple-from-user
    #https://stackoverflow.com/questions/30239092/how-to-get-multiline-input-from-user