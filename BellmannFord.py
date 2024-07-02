g=[
   [0,6,4,5,False,False],
   [False,0,False,False,-1,False],
   [False,-2,0,False,3,False],
   [False,False,-2,0,False,-1],
   [False,False,False,False,0,3],
   [False,False,False,False,False,0]
   ]
d={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F"}
E_L=[]
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j]!=False and g[i][j]!=0:
            E_L.append(tuple((i,j)))
print(E_L)
dist={}
for i in range(len(g)):
    dist[i]=float("inf")
dist[0]=0
print()
print(dist)
print()
for i in range(len(g)-1):
    for j in E_L: 
       new_dist=dist[j[0]]+g[j[0]][j[1]]
       if dist[j[1]]>new_dist:
           dist[j[1]]=new_dist
print(dist)
output:
[(0, 1), (0, 2), (0, 3), (1, 4), (2, 1), (2, 4), (3, 2), (3, 5), (4, 5)]
{0: 0, 1: inf, 2: inf, 3: inf, 4: inf, 5: inf}
{0: 0, 1: 1, 2: 3, 3: 5, 4: 0, 5: 3}
