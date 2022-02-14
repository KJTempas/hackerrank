
def timeConversion(s):
    a_or_p = s[-2:]
    hr = s[0:2]
    #take care of 12Am and 12PM
    if hr =='12' and a_or_p == 'AM':
        return '00'+s[2:-2]
    elif hr == '12' and a_or_p == 'PM':
        return s[0:-2]
    #handle other hours if Am
    elif int(hr)<12 and a_or_p == 'AM':
        return s[0:-2]
    #handle other hours if PM
    else: 
        hr = int(hr) + 12
        return str(hr) + s[2:-2]


print(timeConversion('12:01:00PM')) # '12:01:00
print(timeConversion('12:01:00AM')) # '00:01:00
print(timeConversion('03:30:00AM')) #  '03:30:00
print(timeConversion('03:30:00PM')) # ''15:30:00

