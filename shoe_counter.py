#calculate amount of money earned by shoe store owner
#input [list of shoe sizes', [(cust show size, cost), etc for a list of  customers]]
#not sure about input of shoesize and cost;  or tuple?
#import sys #to get input from command line

def shoe_counter(shoe_sizes,transactions):
    total = 0

    from collections import Counter
    dict = Counter(shoe_sizes)
    print(dict)
    for t in transactions:
        print(t)  
        #if tuple[0] is a key in x(the dictionary made by counter)
        if t[0] in dict.keys():
            print('1', dict[t[0]]) #the value of that key; number of pairs of that size
            if dict[t[0]]>0: #if the value of that key >0
                total += t[1] #add the cost(t[1]) to total
                dict[t[0]] -=1 #reduce the value of that dict item by 1 (reduce # of shoes available)
                print('2',dict[t[0]]) #the new value for that key
                print('t', total)
    print(total)

#function works with this input
#shoe_counter([2,3,4,5,6,8,7,6,5,18], [(6,55), (6,45), (6,55), (4,40), (18, 60), (10,50)])

if __name__ == '__main__':
    #TODO figure out input
    X = input() #number of shoe sizes
    #how to get shoe sizes into shoe sizes []
    shoe_sizes = []
    for n in X:
        n = input()
        shoe_sizes.append(n)
    
   # make tuples size(index [0]) and cost[1]
    N = input() #number of transactions or customers
    transactions = []
    for n in N:
        size = input()
        price = input()
        newtuple = tuple((size, price))
        transactions.append(newtuple)

#     #call method
    shoe_counter(shoe_sizes, transactions)

    #'2' '3' '4' '5' '6' '8' '7' '6' ''5' '10'

    # look at https://stackoverflow.com/questions/19202893/converting-input-from-stdin-into-lists