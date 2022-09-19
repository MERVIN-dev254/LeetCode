# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        my_set = set()
        #nodes = []
        def dfs(node):
            if node is None:
                return False
            nodes.append(node.val)
            y = k - node.val
            if y in my_set:
                return True
            my_set.add(node.val)
            #print (nodes)
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
        
        