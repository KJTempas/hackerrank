#print absolute time difference(t1-t2) in seconds for two UTC times(maybe different time zones
#last 5 digits is time zone)

import datetime
#TODO status - need to resolve issue with %z

def time_delta(t1):
#     strptime converts a string format to datetime - what I need
#     strftime convert a datetime obj to a string format
#    # t1 = t1.ctime()
 
    d1 = datetime.datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    print(d1)
    #TODO problem with z; look into utcoffset() method
    #a = first three char of wkday, %d day of month, %b first 3 char of month, 
    #%Y four digit year, %X time, %z UTC offset
    # t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

    # x = t1-t2
    # print(x)
#TODO look at this
#  d1 = d1.strftime("%Y-%m-%d")
#     d2 = d2.strftime("%Y-%m-%d")
#     return abs((d2 - d1).days)

#https://www.nbshare.io/notebook/510557327/Strftime-and-Strptime-In-Python/
#TODO look at this - problem with z
#https://stackoverflow.com/questions/26165659/python-timezone-z-directive-for-datetime-strptime-not-available
time_delta('Sun 10 May 2015 13:54:36 -0700')#, 'Sun 10 May 2015 13:54:36 -0000') #25200
#time_delta('Sat 02 May 2015 19:54:36 +0530', 'Fri 01 May 2015 13:54:36 -0000') #88200

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
