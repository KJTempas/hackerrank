#given an int, n, print the following values for each integer i 
#from 1 to n
#decimal octal hexadecimal(capitalized) binary
#number can be 1-99; each value shold be space-padded to match the 
#width of the binary value of the number, then separated by a single space
def print_formatted(number):
    #find max length of binary
    l = len(bin(number)[2:])
    print(l)
    print(type(l))
    for i in range(1, number):
        d = i #decimal 
        o = oct(i) #octal
        h = hex(i)
        b = bin(i)[2:] #binary
      
       # print('{:ld} {:ld} {:ld} {:ld} '.format(d, o, h, b))
        print('{:3d}'.format(d))

print_formatted(5)
# 1   1   1     1  #note space padding to match width of binaryvalue
# 2   2   2    10  # values separated by a single space
# 3   3   3    11
# 4   4   4   100
# 5   5   5   101

#if 10, it would be 10 12 A 1010

# if __name__ == '__main__':

