def numPlayers(scores, k):
    n = len(scores)
    #sort scores in descending order
    scores = sorted(scores, reverse=True)
    #initialize a rank array to store the ranks
    rank = []
    #we start at rank 1
    r =1
    #this scores previous scores
    prev = -1
    for i in range(n):
        if prev == -1:
            rank.append(r)
            prev = scores[i]
        elif prev == scores[i]:
            #same rank is added
            rank.append(r)
        else: #diff score values
            prev = scores[i]
            rank.append(i+1)
            #update rank
            r = i +1        
    # rank [1,2,2,4]        
    #counts the number of people whose rank is less than k 
    count = 0        
    for i in range(n):
        if rank[i] <= k and scores[i] != 0:
            count +=1
    return count        


print(numPlayers([100,50,50,25],3))    