# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from lcutils import * 

class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        in_order_list = self.inorder(root)
        
        return in_order_list
        
    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None: 
            return []
        
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    
    
if __name__ == "__main__": 
    
    head = make_tree_node([1,2,3,4,5,6,7])
    ans = Solution().inorderTraversal(root=head)
    print(ans)
    