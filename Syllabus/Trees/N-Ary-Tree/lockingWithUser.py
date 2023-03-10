"""
Problem Description:
We are given an N-ary tree, where each node has a unique ID. We need to implement a locking mechanism for the nodes of the tree. The following operations need to be supported:

lock(id: int, user_id: int) -> bool: Locks the node with the given id if it is not already locked, and sets the lock owner to the given user_id. Returns True if the lock is acquired successfully, False otherwise.

A node can be locked only if none of its ancestors or descendants are locked.
If a node is already locked, the lock can be acquired by the same user who owns the lock.
unlock(id: int, user_id: int) -> bool: Unlocks the node with the given id if it is locked by the given user_id. Returns True if the unlock is successful, False otherwise.

upgrade(id: int, user_id: int) -> bool: Upgrades the lock on the node with the given id to the user with the given user_id if all the descendants of the node are unlocked. Returns True if the upgrade is successful, False otherwise.

A node can be upgraded only if all its descendants are unlocked.
If a node is already locked by the same user who wants to upgrade the lock, the upgrade can be done.

"""


class TreeNode:
    
    def __init__(self, node, parent=None, user=None):
        self.node = node
        self.parent = parent
        self.children = []
        self.locked_by = user
    
    
class Tree:
    
    def __init__(self, root):
        self.tree = {}
        self.tree[root] = TreeNode(root)
        
        
    def add_node(self, node, parent):
        treenode = TreeNode(node, parent)
        self.tree[parent].children(treenode)
    
    def lock(self, node, user):
        if node not in self.tree:
            return False
        if self.tree[node].is_locked != None:
            return False
        if self.is_ancestor_locked(node) or self.is_desendant_locked(node):
            return False
        
        
            
        
    def is_ancestor_locked(self, node):
        ancestor = self.tree[node].parent
        while ancestor:
            if self.tree[ancestor].locked_by != None:
                return True
            ancestor = self.tree[ancestor].parent
        return False
    
    def is_desendant_locked(self, node):
        for child in self.tree[node].children:
            if child.locked_by != None:
                return True
        return False
    
        
    
        
        