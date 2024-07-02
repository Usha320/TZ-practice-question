def bfs(g,e):
    q=[e]
    v={}
    for i in g.keys():
        v[i]=False
    v[e]=True
    while len(q) != 0:
        curr =q.pop(0)
        print(curr,end=" ")
        for i in g[curr]:
            if v[i[1]]==False:
                q.append(i[1])
                v[i[1]]=True
G={1: [(1, 2, 0), (1, 3, 0)], 2: [(2, 1, 0), (2, 5, 0)], 3: [(3, 4, 0), 
        (3, 6, 0)], 4: [(4, 3, 0)], 5: [(5, 2, 0), (5, 7, 0), (5, 10, 0),
        (5, 13, 0)], 6: [(6, 3, 0), (6, 7, 0)], 7: [(7, 5, 0), (7, 6, 0), 
        (7, 8, 0), (7, 9, 0)], 8: [(8, 7, 0)], 9: [(9, 7, 0), (9, 12, 0)], 
        10: [(10, 5, 0), (10, 11, 0)], 11: [(11, 10, 0)], 12: [(12, 9, 0), 
        (12, 13, 0)], 13: [(13, 5, 0), (13, 12, 0)]}
n = int(input('enter the node to traverse: '))
bfs(G,n)
output:
enter the node to traverse: 1
1 2 3 5 4 6 7 10 13 8 9 11 12 
