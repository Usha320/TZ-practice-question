l= {1: [(1, 2, 0), (1, 3, 0)], 2: [(2, 1, 0), (2, 5, 0)], 3: [(3, 4, 0), 
        (3, 6, 0)], 4: [(4, 3, 0)], 5: [(5, 2, 0), (5, 7, 0), (5, 10, 0),
        (5, 13, 0)], 6: [(6, 3, 0), (6, 7, 0)], 7: [(7, 5, 0), (7, 6, 0), 
        (7, 8, 0), (7, 9, 0)], 8: [(8, 7, 0)], 9: [(9, 7, 0), (9, 12, 0)], 
        10: [(10, 5, 0), (10, 11, 0)], 11: [(11, 10, 0)], 12: [(12, 9, 0), 
        (12, 13, 0)], 13: [(13, 5, 0), (13, 12, 0)]}

def dfs(l,v,s,e):
    if v[e]==False:
        s.append(e)
        v[e]=True
    else:
        return
    for i in l[e]:
        dfs(l,v,s,i[1])
    print(s.pop(),end=' ')
    
if __name__ == "__main__":
    v={}
    for i in node:
        v[i]=False
    n= int(input('enter the node to traverse: '))
    s=[]
    dfs(l,v,s,n)
  output:
enter the node to traverse: 1
4 3 6 8 13 12 9 7 11 10 5 2 1 
