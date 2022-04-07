
from collections import OrderedDict

if __name__ == '__main__':
    groc_list = OrderedDict()
    x = int(input())
    for i in range(x):
        entry = input().split()
        price = int(entry[-1])
        product = ' '.join(entry[:-1])
        if product in groc_list:
            #set new value for that key
            price = groc_list[product] + price
            groc_list[product]  = price
        else:
            groc_list[product] = price
    for x,y in groc_list.items():
        print(x, y)

#goal - item name and net price inorder of its first occurrence
#INPUT
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30

#output
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20

#alt answer - note use of rpartition
#The rpartition() method searches for the last occurrence 
# of a specified string, and splits the string into a 
# tuple containing three elements. -> before string, string, after string
#from collections import OrderedDict
# dct = OrderedDict()
# for _ in range(int(input())):
#     i = input().rpartition(" ") #partition at the space
#     dct[i[0]] = int(i[-1]) + dct[i[0]] if i[0] in dct else int(i[-1])
# for l in dct:
#     print(l, dct[l])