class node:
    def __class__init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        self.height=1
def inorder(root):
    if root==None:
        return 
    inorder(root.left)
    print(root.value)
    inorder(root.right)
def ght(root):
    if not root:
        return 0
    else:
        return ght(root.left)-ght(root.right)
def getbf(root):
    if not root:
        return 0
    return ght(root.left)-ght(root.right)
def insert(root,me):
    if not root:
        return node(me)
    if me<root.value:
        root.left=insert(root.left,me)
    else:
        root.right=insert(root.right,me)
    root.height=1+max(ght(root.left),ght(root.right))
    bf=getbf(root)
    if bf>1 and me<root.left.value:#rr rotation
        return rightRotate(root)
    if bf>1 and me>root.left.value:
        root.left=leftRotate(root)
        return rightRotate(root)
    if bf<-1 and me>root.right.value:#ll
        return leftRotate(root)
    if bf<-1 and me<root.left.value:#rl
        root.right=rightRotate(root)
        return leftRotate(root)
    return root
def leftRotate(A):
    b=a.right
    temp=b.left
    b.left=a
    a.right=temp
    a.height=1+max(ght(a.left)-ght(a.right))
    b.height=1+max(ght(b.left)-gth(b.right))
    return b
def rightRotate(A):
    b=a.left
    temp=b.right
    b.right=a
    a.left=temp
    a.height=1+max(ght(a.left)-ght(a.right))
    b.height=1+max(ght(b.left)-gth(b.right))
    return b
if __name__=='__main__':
    root=None
    vl=[19,99,75,7,21,34,38,27,134,100,29,0,12,17,143]
    for i in vl:
        root=insert(root,i)
    inorder(root)
output:
0
7
12
17
19
21
27
29
34
38
75
99
100
134
143
