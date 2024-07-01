
class Node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

def height(root):
    if root==None:
        return 0
    LH=height(root.left)
    RH=height(root.right)
    return max(LH,RH)+1        
if __name__=="__main__":                             
                                            
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

    print("\nheight of the tree is:",height(root))
output:
height of the tree is: 5
