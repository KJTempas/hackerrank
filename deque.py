from collections import deque
#deque is a double ended queue
#can add or remove elements from both ends

d = deque()
for _ in range(int(input())):
    inp = input().split()
    if len(inp)>1:
        #inp[0] is the command, inp[1] is the number
        getattr(d, inp[0])(int(inp[1]))
    else: #because some commands do not have a number with them, like pop
        getattr(d, inp[0])() #need the () because it is pop

print(*[item for item in d])

# #when entering in terminal
# 3
# append 1  - no ' ' needed
# appendleft 4
# append 2