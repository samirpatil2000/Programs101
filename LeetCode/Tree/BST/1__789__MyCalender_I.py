class Treenode:
    def __init__(self,start:int,end:int,left=None,right=None) -> None:
        self.start=start
        self.end=end
        self.left=left
        self.right=right
        
class MyCalendar:
    
    def __init__(self):
        self.root=None
        
    def checker(self,node:Treenode,start:int,end:int):
        curr_start,curr_end=node.start,node.end
        if end<=curr_start:
            if node.left:
                return self.checker(node.left,start,end)
            else:
                node.left=Treenode(start,end)
                return True
        elif start>=curr_end:
            if node.right:
                return self.checker(node.right,start,end)
            else:
                node.right=Treenode(start,end)
                return True
        return False
    
    def book(self, start: int, end: int) -> bool:
        if self.root:
            return self.checker(self.root,start,end)
        else:
            self.root=Treenode(start,end)
            return True

sol=MyCalendar()
x=["MyCalendar", "book", "book", "book"]
y=[[], [10, 20], [15, 25], [20, 30]]
for u,v in y[1:]:
    print(sol.book(u,v))
    
