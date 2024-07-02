class Node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        
class node_data:
    def __init__(self,Node,hkey):
        self.node = Node
        self.hkey = hkey

def topview(root):
    ls=[]
    temp = node_data(root,0)
    q=[temp]
    q.append(None)
    dic={}
    while len(q)>0:
        curr=q.pop(0)
        if curr==None:
            if len(q)==0:
                break
            else:
                q.append(None)
        else:
            
            dic[curr.hkey]= curr.node.value
            
            if curr.node.left!=None:
        
                temp = node_data(curr.node.left,curr.hkey-1)
                q.append(temp)
            if curr.node.right!=None:
                temp = node_data(curr.node.right,curr.hkey+1)
                q.append(temp)
    for i in sorted(dic) :
        print(dic[i])
    
if __name__ == "__main__":                         
                                            
    root=Node(1)                                        
    root.left=Node(2)
    root.right=Node(3)
    
    root.left.left=Node(4)
    root.left.right=Node(5)
    
    root.right.left=Node(6)
    root.right.right=Node(7)
    
    root.left.right.left=Node(9)
    root.left.right.right=Node(10)
    
    root.right.right.right=Node(11)
    
    root.left.right.left.left=Node(12)
    root.left.right.left.right=Node(13) 

    topview(root)
  output:
12
9
13
10
7
11
