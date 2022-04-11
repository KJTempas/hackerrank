
if __name__ == '__main__':
    from collections import namedtuple

    n = int(input())
    cols = input().split()
    total=0
    for _ in range(n):
        #declaring a named tuples with columns provided in input
        students = namedtuple('student', cols) #enter without '    '
        col1, col2, col3, col4 = input().split()
        #making an indiv named tuple
        student = students(col1, col2, col3, col4)
        #add marks for each student to total as they come in
        total += int(student.MARKS)

    print('{:.2f}'.format(total/n))
  
     
        
      
       
  
