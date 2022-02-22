#ex of types of exceptions: ZeroDivisionError, ValueError
#one way to handle exceptions is with try/except

# def py_exceptions(a, b):
#     try:
#         print(int(a)//int(b))
#     except Exception as e: #generic excption
#         print("Error Code:" , e)


# py_exceptions(1,0) #Error Code: integer division or modulo by zero
# py_exceptions(2, '$') #Error Code: invalid literal for int() with base 10: '$'
# py_exceptions(3, 1)  #3

if __name__ == '__main__': #completed (w a little help)
    T = input() # number of test cases 
    for _ in range(int(T)):
        try:
            a,b = map(int, input().split()) #input is a string with space between entries - #must split it and map as integers
            print(int(a)//int(b))
       
        except Exception as e: #generic exception
            print("Error Code:" , e)
