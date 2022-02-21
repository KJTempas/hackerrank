
#completed
def find_percentage(student_marks, query_name):
    scores = student_marks[query_name]
    a = sum(scores)/len(scores)
    return "{:.2f}".format(a)

print(find_percentage({'alpha': [20,30,40], 'beta':[30,50,70]}, 'beta')) #50.00
print(find_percentage({ 'Krishna':[67,68,69], 'Arjun':[70,98,63], 'Malika' :[52,56,60]}, 'Malika') )# 56.00 


# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n): #the _ means whatever
   # #this line means split string by white space, assign name to the first word, then assign line to rest of the words
#         name, *line = input().split() #*line means grab additional returns from the split statement
#         scores = list(map(float, line))
#         student_marks[name] = scores  #dict[key] = value
#     query_name = input()

#     #then method from above goes here
#     scores = ....

#helpful explanation
#https://stackoverflow.com/questions/56658837/how-does-name-line-input-split-work-in-python-3/56658868
# * is the unpacking operator (Python 3+)