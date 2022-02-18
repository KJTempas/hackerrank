#print the results of hashing a tuple made from the list
# Python hash() function is a built-in function and returns the
#  hash value of an object if it has one. 
#  The hash value is an integer which is used to quickly 
# compare dictionary keys while looking at a dictionary.
#only immutable objects are hashable; lists are not hashable

def py_tuple(n,integer_list):
    return hash(tuple(integer_list))


print(py_tuple(2, [1, 2]))

# if __name__ == '__main__':
#     n = int(raw_input())
#     integer_list = map(int, raw_input().split())
    