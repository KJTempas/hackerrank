import re
def regex(s):
    try:
        re.compile(s)
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)

# regex('.*\+') #True
# regex('.*+') #False

#STDIN
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
    # print(s)
        regex(s)