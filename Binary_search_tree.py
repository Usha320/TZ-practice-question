class Node:
    def __init__(self,data):
        self.value=data
        self.right=None
        self.left=None
def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.value,end=' ')
    inorder(root.right)
def bst(root,val):
    if root==None :
        root = Node(val)
        return root
    if  val<root.value:
        root.left=bst(root.left,val)
    else:
        root.right=bst(root.right,val)
    return root
    
if __name__ == "__main__":
    n= list(map(int,input().split()))
    node = Node(n[0])
    for i in range(1,len(n)):
        node=bst(node,n[i])
    inorder(node)
output:
4 6 7 3 8 2 5 9 1
1 2 3 4 5 6 7 8 9
        
