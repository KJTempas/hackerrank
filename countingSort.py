def countingSort(arr): #completed
    results = [0] * 100 #set up empty array of correct length
    for i in range(len(arr)): #loop through numbers in array by index
        #add one to the results array at the index of that number
        results[arr[i]] = results[arr[i]] + 1
        
    return results
        

countingSort([1,1,3,2,1]) #[0,3,1,1]
countingSort([1,2,3,4,3,2,3]) #[0,1,2,3,1,0,0...]

