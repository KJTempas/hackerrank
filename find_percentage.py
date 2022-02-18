
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
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()

#     #then method from above goes here
#     scores = ....