class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
    
def preorder(root):
    if root == None:
        return
    print(root.value,end=' ')
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.value,end=' ')
    inorder(root.right)

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value,end=' ')

if __name__ == "__main__":
    root = node(1)
    root.left = node(2)
output:pre-order
1 2 4 5 3 6 7 
in-order
4 2 5 1 6 3 7 
post-order
4 5 2 6 7 3 1 
