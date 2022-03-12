#print absolute time difference(t1-t2) in seconds for two UTC times(maybe different time zones
#last 5 digits is time zone)

#import datetime
#TODO status - need to resolve issue with %z

# def time_delta(t1,t2):
# #     strptime converts a string format to datetime - what I need
# #     strftime convert a datetime obj to a string format
# #    # t1 = t1.ctime()
#     d1 = datetime.datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
#     print(d1)
#     d2 = datetime.datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
#     print(d2)
#     return int(abs(d1-d2).seconds)
    #TODO problem with z; look into utcoffset() method
    #a = first three char of wkday, %d day of month, %b first 3 char of month, 
    #%Y four digit year, %X time, %z UTC offset

#https://www.nbshare.io/notebook/510557327/Strftime-and-Strptime-In-Python/
#TODO look at this - problem with z
#https://stackoverflow.com/questions/26165659/python-timezone-z-directive-for-datetime-strptime-not-available
#time_delta('Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 -0000') #25200
#time_delta('Sat 02 May 2015 19:54:36 +0530', 'Fri 01 May 2015 13:54:36 -0000') #88200

#another's code - when I run, I get a ValueError: 'z' is a bad directive in format '%a.....%z'
# from datetime import datetime as dt
# def time_delta(t1,t2):
#     fmt = '%a %d %b %Y %H:%M:%S %z'
#     for i in range(int(input())):
#         print(int(abs((dt.strptime(input(), fmt) - 
#                     dt.strptime(input(), fmt)).total_seconds())))

# time_delta('Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 -0000') #25200

# #another soln
# import datetime
# import time

# maxT = int(raw_input())
# for outer_counter in xrange(maxT):
#     T = [0, 0]
#     for i in xrange(2):
#         my_input = raw_input()
#         my_input = [my_input[:-6], int(my_input[-5:])]
#         if my_input[1] == 0:
#             minute_shift = 0
#         else:
#             minute_shift, my_input[1] = my_input[1]/abs(my_input[1]), abs(my_input[1])
#             minute_shift = minute_shift * ( (my_input[1]//100)*60 + my_input[1]%100 )
#         T[i] = datetime.datetime.strptime(my_input[0],'%a %d %b %Y %H:%M:%S') - datetime.timedelta(minutes=minute_shift)
#     print abs(long((T[0]-T[1]).total_seconds()))

# #this provided in challenge
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     t = int(input())
#     for t_itr in range(t):
#         t1 = input()
#         t2 = input()
#         delta = time_delta(t1, t2)
#         fptr.write(delta + '\n')
#     fptr.close()
