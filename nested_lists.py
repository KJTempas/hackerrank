
#Given list of students and scores; print the names of any student(s)
#having the second lowest grade.  If there are mult students, order 
#their names alphabetically and print each one on a line
#https://betterprogramming.pub/10-important-tips-for-using-nested-lists-in-python-38ceca68be35


#why does this not work in HackerRank?
def nested_lists(records):
    #convert nested list to dict
    dict = {}
    for sub_list in records:
        dict[sub_list[0]] = sub_list[1] #dictname[key] = value
    #remove min key value
    min_value = min(dict.values())
    for key,value in dict.items():
        if value == min_value:
            del dict[key]
            
    #find min again
    min_value =min(dict.values())

    dict_items = dict.items()
    sorted_items = sorted(dict_items) #sort alphabetically by key
    for s in sorted_items: #loop through tuple
        if s[1] == min_value:
            print(s[0])


nested_lists([['chi', 20.0],['beta', 50.0], ['alpha', 50.0]]) #alpha beta
nested_lists([['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]) # Berry Harry
nested_lists([['Beria', 20], ['Varun', 19], ['Harsh', 20], ['Kakunami', 19], ['Vikas', 21]]) #Beria, Harsh
#original in hackerrank
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())



#this almost works but fails 2/10 test cases
# checkout one failed test case - it is line 32 above, which works on my code above
# if __name__ == '__main__':
#     records = []
#     for _ in range(int(input())): #these input lines provided
#         name = input()
#         score = float(input())

#         records.append([name, score])

#     dict = {}
#     for sub_list in records:
#         dict[sub_list[0]] = sub_list[1] #dictname[key] = value
#     #remove min key value
#     min_value = min(dict.values())
#     for key,value in dict.items():
#         if value == min_value:
#             del dict[key]
#             
#     #find min again
#     min_value =min(dict.values())

#     dict_items = dict.items()
#     sorted_items = sorted(dict_items) #sort alphabetically by key
#     for s in sorted_items: #loop through tuple
#         if s[1] == min_value: #if the value in the tuple is the min
#             print(s[0])