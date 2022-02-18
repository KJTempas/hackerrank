def capitalize(s): #completed
    #split string at spaces if there are any
    st = s.split(' ')
    res = ''
    for x in st:
        res += x.capitalize() + ' '
    return res

# capitalize('chris alan') #Chris Alan
# capitalize('12abc') #12abc
# print(capitalize('12abc alan'))
print(capitalize(' hello   world  lol'))  #extra spaces need to be retained

#why does this not work ?
# if __name__ == '__main__': 
#     s = input()
#     # import pdb
#     # breakpoint()
#     print(capitalize(s))



