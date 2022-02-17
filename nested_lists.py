
#Given list of students and scores; print the names of any student(s)
#having the second lowest grade.  If there are mult students, order 
#their names alphabetically and print each one on a line
#https://betterprogramming.pub/10-important-tips-for-using-nested-lists-in-python-38ceca68be35

def nested_lists(records):
    #convert nested list to dict
    dict = {}
    for sub_list in records:
        dict[sub_list[0]] = sub_list[1]
    #remove min key value
    min_value = min(dict.values())
    for key,value in dict.items():
        if value == min_value:
            del dict[key]
            break
    #find min again
    min_value =min(dict.values())
    for key,value in dict.items():
        if value == min_value:
            print(key)

#TODO make sure if mult students, order of names is alphabecital

nested_lists([['chi', 20.0],['beta', 50.0], ['alpha', 50.0]]) #alpha beta
nested_lists([['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]) # Berry Harry

# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())