class Node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

def levelorder(root):
    q=[root]
    q.append(None)
    while len(q)>0:
        curr=q.pop(0)
        if curr==None:
            if len(q)==0:
                return
            -+
            else:
                print()
                q.append(None)
        else:
            print(curr.value,end=" ")
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)
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
    
    levelorder(root)
output:
1 
2 3 
4 5 6 7 
9 10 11 
12 13 
