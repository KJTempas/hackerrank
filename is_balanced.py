
# a sequence of brackets is balanced if the following conditions are met:
# It contains no unmatched brackets.
# The subset of brackets enclosed within the confines of a matched pair of 
# brackets is also a matched pair of brackets.

def isBalanced(s):
    #if { is at position 0, } must be at position -1 .... working inward
    forward = [ i for i in s]  #string to list
    revers = forward[::-1]  #reverse the string - slice [::-1]
   #tried zipping; doesn't help
    #find forward[0] in dictionary as key; value must be revers[0], but only for first half of lists
    dict = {'{': '}', '[':']', '(':')'}  # dictionary of matching brackets
    #TODO this does not work if brackets are paired w/in - need different approach
    #only need to compare first half of lists
    for i in range(int(len(forward)/2)):         #dict[key]!=value
       # print(forward[i])
        if forward[i] in dict.keys() and dict[forward[i]] == revers[i]:
            continue  
        else:
            return 'NO'
    return'YES'


print(isBalanced('{[()]}')) #YES
print(isBalanced('{[(])}')) #NO
print(isBalanced('{{[[(())]]}}')) #YES
print(isBalanced('{{)[](}}')) #NO 
print(isBalanced('{(([])[])[]}')) #YES
print(isBalanced('{(([])[])[]}[]')) #YES

# #input provided
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         s = input()

#         result = isBalanced(s)

#         fptr.write(result + '\n')

#     fptr.close()