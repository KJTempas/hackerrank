# Dense ranking = player w/ highest score is 1;
# Players w = scores get same ranking and next player(s)
# get rank immed. after 
# ex. 1, 2,2,3 if score [100,90,90,80]
# Given leaderboard score(ranks) an new players scores,
# determine the new playe's rank after each score

def climbingLeaderboard(ranked, player):
    #find original ranks
    ranks =[]
    i = 1
    for r in range(0, len(ranked)-1): #loop through ranked scores
        print(ranked[r])
        if ranked[r] > ranked[r+1]:
            ranks.append(i)
            print('ranks1',ranks)
            i+=1
            #how many are the same if equal? count?
        elif ranked[r] == ranked[r+1]:
            x = ranked.count(ranked[r])
            for t in range(x):
                ranks.append(i) #append rank multiple times
                print('2',ranks)
            i +=1
            r +=x
#tried scipy.stats - not appropriate for this type of ranking
 #y = [sorted(ranked).index(x) for x in ranked] #does not work either
    
    #add new score to ranked, then rerank each time
    #make ranking a function  or use a while loop



#subtask - for 60% of max score: 1<=n<=200 and same for m

climbingLeaderboard([100,90,90,80], [70,80,105]) # [4 3 1]
#climbingLeaderboard([100,100,50,40,40,20,10], [5, 25,50,120]) #[6 4 2 1]
#climbingLeaderboard([100,90,90,80,75,60],[50,65,77,90,102])# [6 5 4 2 1]

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