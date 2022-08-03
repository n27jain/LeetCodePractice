# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(None,root,None)
        return
    
    def helper(self,prev,node,isLeft):
        # traverse Left, right, root

        if(node == None):
            return
        self.helper(node,node.left, True)
        self.helper(node,node.right, False)
        if prev == None:
            return True
        if isLeft and prev.val <= node.val:
            return False
        if not(isLeft) and prev.val >= node.val:
            return False
        

