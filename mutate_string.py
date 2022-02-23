
#read a given string, change the character at a given index and then 
#print the modified string
#answer give in challenge

def mutate_string(string, position, character):
    print(string[0:position] + character + string [position+1:])


#mutate_string('abracadabra', 5, 'k')

if __name__ == '__main__':
    string = input()
    position, character  = input().split()
    position = int(position)
    
    #alt input and call strategy
    #  s = input()
    # i, c = input().split()
    # s_new = mutate_string(s, int(i), c)
    # print(s_new)
    
    mutate_string(string, position, character)