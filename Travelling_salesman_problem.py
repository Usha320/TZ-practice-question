import sys            
def Cost(curr,visited,G,DP):
    n=len(G)
    if len(visited)==n:
        return G[curr][0] 
    visit=tuple(visited)
    if (curr,visit) in DP:
        return DP[(curr,visit)]
    #min=float("inf")
    min_cost=sys.maxsize
    for i in range(n):
        if i not in visited:                                
            new_visit=visited+[i]
            new_cost=G[curr][i]+Cost(i,new_visit,G,DP) 
            min_cost=min(min_cost,new_cost)
    DP[(curr,visit)]=min_cost
    return min_cost
           
G=[
   [0,4,7,5,5],
   [4,0,2,3,8],
   [7,2,0,3,4],
   [5,3,3,0,6],
   [5,8,4,6,0],
   ]
n=len(G)
DP={} 
print("Minimum Cost = ", Cost(0,[0],G,DP))
for i in DP:
    print(i)
output:
Minimum Cost =  19
(3, (0, 1, 2, 3))
(4, (0, 1, 2, 4))
(2, (0, 1, 2))
(2, (0, 1, 3, 2))
(4, (0, 1, 3, 4))
(3, (0, 1, 3))
(2, (0, 1, 4, 2))
(3, (0, 1, 4, 3))
(4, (0, 1, 4))
(1, (0, 1))
(3, (0, 2, 1, 3))
(4, (0, 2, 1, 4))
(1, (0, 2, 1))
(1, (0, 2, 3, 1))
(4, (0, 2, 3, 4))
(3, (0, 2, 3))
(1, (0, 2, 4, 1))
(3, (0, 2, 4, 3))
(4, (0, 2, 4))
(2, (0, 2))
(2, (0, 3, 1, 2))
(4, (0, 3, 1, 4))
(1, (0, 3, 1))
(1, (0, 3, 2, 1))
...
(2, (0, 4, 3, 2))
(3, (0, 4, 3))
(4, (0, 4))
(0, (0,))
