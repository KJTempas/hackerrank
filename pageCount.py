#find min number of pages that must be turned to arrive at page p 
#give the book is n pages long; pg 1 is always rt hand page
#can turn from back or front of book
def pageCount(n,p): #correct
    #from front of book
    p= p+1 if p%2!=1 else p
    front = p//2
    #from back of book
    n=n+1 if n%2!=1 else n
    back = (n-p)//2
    #find min of two values -front and back
    return min(front, back)

pageCount(5,3) #1
pageCount(10, 4) #would be 2 from front and 3 from back, so 2
pageCount(13, 6) # 3 front, 3 back ; 3
pageCount(15, 9) #  4 front, 3 back; 3
print(pageCount(15, 5)) # 2 front, 5 back
