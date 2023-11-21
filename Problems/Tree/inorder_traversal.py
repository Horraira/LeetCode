
################ question ################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

hot = TreeNode('Hot')
cold = TreeNode('Cold')
newTree = TreeNode('Drink', hot, cold)

class Solution:
    def inOrderTraversal(self, root):
        result = []
        def inOrder(root):
            if root:
                inOrder(root.left)
                result.append(root.val)
                inOrder(root.right)
        inOrder(root)
        return result
        
sol1 = Solution()
print(sol1.inOrderTraversal(newTree))
print(sol1.inOrderTraversal(hot))

################ suggested solution 1 ################
# def inorder(root):
#   return  inorder(root.left) + [root.val] + inorder(root.right) if root else []

################ suggested solution 2 ################
################ without recursion ################

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