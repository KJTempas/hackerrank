
#compute average of all plants w distinct heights in greenhouse
#given list of all plant heights return float value rounded to 3places after decimal

def average(arr): #completed
    result= sum(set(arr))/len(set(arr))
    return ('{:.3f}'.format(result))

#average([161,182,161,154,176,170,167, 171, 170, 174]) #169.375


if __name__ == '__main__':
    n = int(input())
    #when using stdinput, enter N(size of arr) on first line, 
    # then array in a string  on second line  like this '1 2 3 3'
    #this means make a list by mapping each input as an int by splitting the input string
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

