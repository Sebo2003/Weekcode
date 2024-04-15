#LEETCODE 701
#Note: The Node class is already made and the BST is already populated. Just focus on inserting
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return root
        #This is a pointer-based BST
        #I need to traverse it to know where to insert my Target node
        #Therefore, I can simply compare values of Nodes to determine whether I should go left or right
        #(Do I *HAVE* to use pre/in/post order traversal??(Hint: Yes, this does build off the easy answer!))
        #This will be done recursivley (figure out the break condition yourself this time)(Hint)

    # This merely prints your answer, don't focus on this method
    def printTree(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result
        
        
if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    target = 2
    result = sol.searchBST(root, target)
    if result:
        print(sol.printTree(result)) 


