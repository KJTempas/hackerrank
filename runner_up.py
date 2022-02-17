#given list of scores, find the runner-up score

def runner_up(arr):
    to_set = set(arr)  #to set to remove duplicates
    arr = list(to_set)     #back to list
    arr.remove(max(arr)) #find max and remove it from list
    return max(arr) #return new max (runner up)

print(runner_up([2,3,6,6,5])) #5