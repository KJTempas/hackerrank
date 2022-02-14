#given square grid of chars in a-z, rearrange elements of each row alphab
#determine if columns are also in asc alphab order top to bottom
#return Yes if they are, NO if not

def gridChallenge(grid):
    #this solved all but one test case(#4 below?)
    new_grid = []
    for r in grid: #each row in the grid
        sort_str = sorted(r)
        r = "".join(sort_str)
        new_grid.append(r)
        #now each row in alphabetical order
        #now check if in alphabetical order in columns
    print(new_grid)
    for x in range(len(new_grid)-1):
        for y in range(len(new_grid)-1):
            # print(new_grid[x][y])
            # print(new_grid[x+1][y])
            if new_grid[x][y]> new_grid[x+1][y]:
                return 'NO'
    return 'YES'

    

#print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'])) #YES
#print(gridChallenge(['zzzzz', 'fghij', 'olmkn', 'trpqs', 'xywuv'])) #NO
print(gridChallenge(['abc', 'ade', 'efg'])) #YES
print(gridChallenge(['eibjbwsp', 'ptfxehaq', 'jxipvfga', 'rkefiyub', 'kalwfhfj', 'lktajiaq','srdgoros','nflvjznh']))

