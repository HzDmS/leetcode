# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        del_set, ret = set(), []
        for node in to_delete:
            del_set.add(node)
            
        def dfs(node):
            
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)
            
            if node.val in del_set:
                # current node needs to be deleted.
                if node.left and node.left.val not in del_set:
                    ret.append(node.left)
                if node.right and node.right.val not in del_set:
                    ret.append(node.right)
            else:
                # child node needs to be deleted.
                if node.left and node.left.val in del_set:
                    node.left = None
                if node.right and node.right.val in del_set:
                    node.right = None

        dfs(root)
        if root.val not in del_set:
            ret.append(root)
        return ret
        
