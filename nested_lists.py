
#Given list of students and scores; print the names of any student(s)
#having the second lowest grade.  If there are mult students, order 
#their names alphabetically and print each one on a line
#https://betterprogramming.pub/10-important-tips-for-using-nested-lists-in-python-38ceca68be35


def nested_lists(records):
    x = min(records, key=lambda x: x[1])  #the min value of each list, comparing the second element
    #filter list, removing if value is == min
    new_records = [ele for ele in records if ele[1]!=x[1]]
    #find min again
    x = min(new_records, key=lambda x: x[1])
    final_records = [ele for ele in new_records if ele[1]==x[1]]
    #sort records by name, alphabetically
    final_records.sort()
    for record in final_records:
        print(record[0])


nested_lists([['chi', 20.0],['beta', 50.0], ['alpha', 50.0]]) #alpha beta
nested_lists([['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]) # Berry Harry
nested_lists([['Beria', 20], ['Varun', 19], ['Harsh', 20], ['Kakunami', 19], ['Vikas', 21]]) #Beria, Harsh
# 
# if __name__ == '__main__':
#     records = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         records.append([name, score])
# nested_lists(records)



