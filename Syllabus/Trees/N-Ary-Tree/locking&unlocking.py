class TreeNode:
    def __init__(self, node, parent):
        self.node = node
        self.children = []
        self.is_locked = False
        self.parent = parent

class Tree:
    
    def __init__(self, root):
        self.tree = {}
        self.tree[root] = TreeNode(root, None)
        
    def is_locked(self, node):
        if node in self.tree:
            return self.tree[node].is_locked
        return False
        
    def _is_ancestors_are_locked(self, node):
        ancestor = self.tree[node].parent
        while ancestor:
            if ancestor.is_locked:
                return True
            ancestor = self.tree[ancestor].parent
        return False
    
    def _is_descendants_are_locked(self, node):
        for child in self.tree[node].children:
            if child.is_locked:
                return True
            return self._is_descendants_are_locked(child)
        return False
    
    def unlock(self, node):
        self.tree[node].is_locked = False
        return
        