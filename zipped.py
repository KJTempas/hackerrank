
#N = number of students
#X = number of subjects

if __name__ == '__main__':
    A = []
    N,X = map(int,input().strip().split())
    for _ in range(X):
        b = list(map(float,input().strip().split()))
        A.append(b)
    b = zip(*A) #yields a zip object each part is a tuple
    for i in b: #unpack zip and sum/divide by X
        print(sum(i)/X)

   #sample input 
#     5 3
#columns are students, rows are subjects
# 89 90 78 93 80 #scores for subject 1
# 90 91 85 88 86  #scores for subject 3
# 91 92 83 89 90.5
#output 
#90.0 
#91.0 
#82.0
#90.0
#85.5