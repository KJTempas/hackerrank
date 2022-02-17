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
    # l = len_new_grid
    # for x in range(len(new_grid)-1):
    #     #TODO rethink this area
    #     for y in range(len(new_grid)-1):
    #         print(new_grid[x][y])
    #         print(new_grid[x][y+1])
    #         if new_grid[x][y]> new_grid[x+1][y]:
    #             return 'NO'
    # return 'YES'

#TODO look at pandas.DataFrane.T to invert/transpose 2D list(swap rows and column s)
#https://note.nkmk.me/en/python-pandas-t-transpose/
    #alt plan
    l = len(new_grid)
    print(l)
    for x in range(l):
         for y in range(l-1):
            print(y,x)
            print(new_grid[y][x])
            print(new_grid[y+1][x])
            if new_grid[y][x] < new_grid[y+1][x]:
                return 'NO'
    return 'YES'
  #  0,0; 0,1; 0,2; ... 1,0; 1,1; 1,2

# print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'])) #YES
# print(gridChallenge(['zzzzz', 'fghij', 'olmkn', 'trpqs', 'xywuv'])) #NO
#print(gridChallenge(['abc', 'ade', 'efg'])) #YES
print(gridChallenge(['abc', 'adh', 'efg'])) #NO
#print(gridChallenge(['eibjbwsp', 'ptfxehaq', 'jxipvfga', 'rkefiyub', 'kalwfhfj', 'lktajiaq','srdgoros','nflvjznh']))

