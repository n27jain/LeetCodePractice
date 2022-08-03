# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.layers = [[]]
        self.len = 0
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return None
        self.inorderTraversal(root, 0 )
        return self.layers
        
    def inorderTraversal(self, node, i):
        if node == None:
            return
        if i > self.len:
            self.layers.append([node.val])
            self.len += 1
        else:
            self.layers[i].append(node.val)
        self.inorderTraversal(node.left, i + 1)
        self.inorderTraversal(node.right, i + 1)
        return