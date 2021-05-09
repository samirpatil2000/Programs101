class newNode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None

root = newNode(50)

root.left=newNode(25)
root.left.left=newNode(12)
root.left.right=newNode(37)
root.left.right.left=newNode(30)
root.left.right.right=newNode(40)

root.right=newNode(75)
root.right.right=newNode(87)
root.right.left=newNode(62)
root.right.left.right=newNode(70)
root.right.left.left=newNode(60)