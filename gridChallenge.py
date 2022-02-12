def gridChallenge(grid):
    #this solved all but one test case(#4 below)
    alpha_rows = []
    for g in grid:
        sort_str = sorted(g)
        g = "".join(sort_str)
        alpha_rows.append(g)
        #now each row in alphabetical order
        #now check if in alphabetical order in columns
    print(alpha_rows)
    for x in range(0,len(alpha_rows)-1):
        for y in range(0, len(alpha_rows)-1):
            if alpha_rows[x][y]<= alpha_rows[x+1][y]:
                continue
            else:
                return 'NO'
    return 'YES'

    #another's solution'
def gridChallenge(grid):
  
    res = True
    y = len(grid[0])

    for i in range(n):
        grid[i] = sorted(grid[i])
    
    for a in range(n-1):
        for b in range(y):
            if grid[a][b] > grid[a+1][b]:
                res = False
    return "YES"  if res else "NO"

#another solutin
def gridChallenge(grid):
   
    for i in range(len(grid)):
        new=sorted(grid[i])
        grid[i]=''.join(new)
    for m in range(len(grid[0])):
        for n in range(len(grid)-1):
            if grid[n][m]>grid[n+1][m]:
                return 'NO'
    return 'YES'
#print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'])) #YES
#print(gridChallenge(['zzzzz', 'fghij', 'olmkn', 'trpqs', 'xywuv'])) #NO
#print(gridChallenge(['abc', 'ade', 'efg'])) #YES
#print(gridChallenge(['eibjbwsp', 'ptfxehaq', 'jxipvfga', 'rkefiyub', 'kalwfhfj', 'lktajiaq','srdgoros','nflvjznh']))
