# Dense ranking = player w/ highest score is 1;
# Players w = scores get same ranking and next player(s)
# get rank immed. after 
# ex. 1, 2,2,3 if score [100,90,90,80]
# Given leaderboard score(ranks) and new players scores,
# determine the new playe's rank after each score

#this works for pretests and some test cases, but 
# Terminated due to timeout on several test cases;
# unlocked one - data set is huge
#there must be a more efficient way to handle data

def climbingLeaderboard(ranked, player):
    res =[] #for rank each time new player score added
    for p in player:     #loop through player scores
        #add score to ranked
        ranked.append(p)
        #change to set to remove dups
        ranked_set = set(ranked)
        #back to list, then sort
        n_ranked = list(ranked_set)
        new_ranked = sorted(n_ranked,reverse=True)
        x = new_ranked.index(p)  # get index of p in new_ranked
        res.append(x+1)  #so not zero based

    return res
 #generator expression
 #binary   - binary search
#subtask - for 60% of max score: 1<=n<=200 and same for m

print(climbingLeaderboard([100,90,90,80], [70,80,105])) # [4 3 1]
print(climbingLeaderboard([100,100,50,40,40,20,10], [5, 25,50,120])) #[6 4 2 1]
print(climbingLeaderboard([100,90,90,80,75,60],[50,65,77,90,102]))# [6 5 4 2 1]

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ranked_count = int(input().strip())

#     ranked = list(map(int, input().rstrip().split()))

#     player_count = int(input().strip())

#     player = list(map(int, input().rstrip().split()))

#     result = climbingLeaderboard(ranked, player)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()



#old method

# # def rank_players(ranked):
#     #find original ranks
#         new_ranks =[]
#         i = 1 #rank starts here
#         for r in range(len(ranked)-1): #loop through ranked scores
#            # print(ranked[r])
#             if ranked[r] > ranked[r+1]:
#                 new_ranks.append(i)
#                 #print('ranks1',ranks)
#                 if ranked[r] == p:
#                     res.append(i)
#                 i+=1
#                 #how many are the same if equal? count?
#             elif ranked[r] == ranked[r+1]:
#                 x = ranked.count(ranked[r])
#                 for t in range(x):
#                     new_ranks.append(i) #append rank multiple times
#                     if ranked[r] == p:
#                         res.append(i)
#                     print('2',new_ranks)
#                 i +=1
#                 r +=x
#                 #where is p in the ranks?
#         #need to deal with last num in ranked gets rank i+1
#         ranks.append(i+1)
#     print('res', res)