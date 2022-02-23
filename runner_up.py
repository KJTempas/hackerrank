#given list of scores, find the runner-up score

def runner_up(arr): #completed 
    to_set = set(arr)  #to set to remove duplicates
    arr = list(to_set)     #back to list
    arr.remove(max(arr)) #find max and remove it from list
    return max(arr) #return new max (runner up)

#print(runner_up([2,3,6,6,5])) #5


if __name__ == '__main__':

   # n=int(input()) #number of elements in array #really needed?
    arr = map(int, input().split())

    print(runner_up(arr))


    #how do you get this to run from main?