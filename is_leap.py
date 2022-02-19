#aka Write a function
#3 conditions to identify a leap year
#the year can be evenly divided by 4 is a leap year unless
#the year can be evenly divided by 100 is NOT a leap year unless
#the year is also evenly divicible by 400.  Then it is a leap year

def is_leap(year):
    # if year % 4 == 0: #is a leap year unless
    #     if year % 100 == 0: #is not a leap year unless
    #         if year % 400 == 0: #is a leap year
    #             print('True')
    #     print('False')
    #TODO figure it out
    if year % 400 == 0 and year % 100 ==0:
        if year % 100 !=0 and year %400 == 0:
            print('True')
    else:
        print('False')

is_leap(1800) #False
is_leap(2000) #True
# is_leap(1990) #False

# if __name__ == '__main__':
#     year = int(input())

#     is_leap(year)