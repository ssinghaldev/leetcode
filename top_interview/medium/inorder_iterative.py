# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        ans = []
        stack = []
        
        stack.append((root, 1))
        while stack:
            node, i = stack.pop()
            if i == 1:
                if node.right:
                    stack.append((node.right, 1))
                
                stack.append((node,2))
                
                if node.left:
                    stack.append((node.left, 1))
        
            elif i == 2:
                ans.append(node.val)
        
        return ans
