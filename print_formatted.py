#aka string formatting
#given an int, n, print the following values for each integer i 
#from 1 to n
#decimal octal hexadecimal(capitalized) binary
#number can be 1-99; each value shold be space-padded to match the 
#width of the binary value of the number, then separated by a single space
def print_formatted(number):
    #find max length of binary
    l = len(bin(number)[2:])
    #l = len("{0:b}".format(number)) #alt way to do it
 
    for i in range(1, number+1):
       #o for octal, d for decimal, X for capitalized  hex, b for binary
        #{column:{width of column}decimal or binary...} remeber to add l to format
        print("{0:{l}d} {1:{l}o} {2:{l}X} {3:>{l}b}".format(i,i,i,i, l = l))
        
  #tricky formatting; lea rned about o and X and b

print_formatted(5)
# 1   1   1     1  #note space padding to match width of binaryvalue
# 2   2   2    10  # values separated by a single space
# 3   3   3    11
# 4   4   4   100
# 5   5   5   101

#if 10, it would be 10 12 A 1010

# if __name__ == '__main__':

