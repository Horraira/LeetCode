
################ question ################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        if not root:
            return None
        else:
            self.inorderTraversal(root.left)
            lst.append(root.val)
            self.inorderTraversal(root.right)
        return lst

################ suggested solution 1 ################
# def inorder(root):
#   return  inorder(root.left) + [root.val] + inorder(root.right) if root else []

################ suggested solution 2 ################
### without recursion

# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         st = []
#         res = []

#         while root or st:
#             while root:
#                 st.append(root)
#                 root = root.left
            
#             root = st.pop()
#             res.append(root.val)

#             root = root.right
        
#         return res  