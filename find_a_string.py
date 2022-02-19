# called count_substring or count_substring

def count_substring(string, sub_string): #completed
    #using regex doesn't get overlapping substrings
    # x = re.findall(sub_string, string)
    # print(x)
    # print(len(x))
    #below does
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(sub_string, start) #find only finds one occurrence
        if pos != -1: #meaning a match was found)
            start = pos +1  #move start to the next position
            count +=1 #add to the counter
        else: 
            break
    return count

#print(count_substring('ABCDCDC', 'CDC')) #2
 #help from https://www.geeksforgeeks.org/python-count-overlapping-substring-in-a-given-string/

if __name__ == '__main__':
    string = input()
    sub_string = input() #enter input in string '    '

    print(count_substring(string,sub_string))