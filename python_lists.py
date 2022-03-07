

if __name__ == '__main__':
    N = int(input()) 
    arr = []
    for _ in range(0, int(input())):
        user_input = input().split(' ')
        cmd = user_input.pop(0) #remove first part of input
        if len(user_input)>0 :#if remaining input
            if 'insert' == cmd:
                eval("L.{0}({1}, {2})".format(cmd, user_input[0], user_input[1]))
            else:
                eval("L.{0}({1})".format(cmd, user_input[0]))
        elif cmd == 'print':
            print L
        else:
            eval("L.{0}()".format(cmd))      
   
    for c in cmds:
        x = c.split()
        t = x[0]
        if len(x)==2:
            y = int(x[1])
        if len(x) == 3:
            y = int(x[1])
            z = int(x[2])

#alt answer to investigate
L = []
for _ in range(0, int(raw_input())):
    user_input = raw_input().split(' ')
    command = user_input.pop(0)
    if len(user_input) > 0:
        if 'insert' == command:
            eval("L.{0}({1}, {2})".format(command, user_input[0], user_input[1]))
        else:
            eval("L.{0}({1})".format(command, user_input[0]))
    elif command == 'print':
        print L
    else:
        eval("L.{0}()".format(command))

#alt answer to understand
#python_lists(['insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 'print', 'pop', 'reverse', 'print'])


  
