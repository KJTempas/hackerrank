#python lists

if __name__ == '__main__':
    N = int(input()) # number of commands
    arr = []
    for _ in range(N):
        s = input().split()
        command = s[0] 
        if len(s)==2:
            s[1] = int(s[1]) 
        if len(s)==3:
            s[1] = int(s[1])
            s[2] = int(s[2])
        if command == 'insert':
            arr.insert(s[1], s[2]) 
        elif command == 'remove':
            arr.remove(s[1])
        elif command == 'append':
            arr.append(s[1])
        elif command == 'sort':
            arr.sort()
        elif command == 'pop':
            arr.pop()
        elif command == 'reverse':
            arr.reverse()
        else:
            print(arr)
       

# #alt answer to investigate
# L = []
# for _ in range(0, int(raw_input())):
#     user_input = raw_input().split(' ')
#     command = user_input.pop(0)
#     if len(user_input) > 0:
#         if 'insert' == command:
#             eval("L.{0}({1}, {2})".format(command, user_input[0], user_input[1]))
#         else:
#             eval("L.{0}({1})".format(command, user_input[0]))
#     elif command == 'print':
#         print L
#     else:
#         eval("L.{0}()".format(command))


