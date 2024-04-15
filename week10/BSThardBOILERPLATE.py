
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeFromBST(self, root: Optional[TreeNode], remove: int) -> Optional[TreeNode]:
        if root is None:
            return None

        #I must remove a node to solve this problem
        #But removing nodes can violate the integrity of BST
        #So, I should replace the values of the nodes I delete with some other value that doesn't violate the BST
        #It should probably be the value of one of their children
        #But what if they have 2 children, or no children at all?
        #What if the children have children, what then?!
        #Hmmmm........

        return root
    

    #here's a method that you can use to solve this problem! Big hint here!
    def findSuccessor(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

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

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)

    remove = 5
    result = sol.removeFromBST(root, remove)
    if result:
        print(sol.printTree(result))