"""
LEETCODE 700
_______________________________________________________________________________________________
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If 
such a node does not exist, return null.

Example 1:

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []
 
Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 10^7
root is a binary search tree.
1 <= val <= 10^7
_______________________________________________________________________________________________
LOGIC:
_______________________________________________________________________________________________
This problem is looking for some random value in a Binary Search Tree. This explanation assumes you know the 
properties of BSTs.

Because the Target value is known, and because BSTs are naturally sorted, we can simply work our way down the
Tree in accordance to the value of a Node's Left and Right Child.

searchBST() is given two parameters: an array of Nodes [essentially a BST] and a Target. We solve this problem
recursivley, as it is the easiest looping methodology to write.

First, let us implement the case of being giving an empty tree: if root is None: return None. "If we have nothing,
give nothing"

Now, lets write our recursive break condition: if root.val == target: return root. Note, "root" is derived of
the TreeNode class, which has three fields: val, left, and right. Val is the Node's data, and left and right
can be thought of as pointers poitning to a Node's left and right Child. So, when we write: if root.val == target,
we are saying "Is this the Node we're looking for?". If it is, return that Node (return root)

Now, lets write our loop. First, check whether the value of our current Node is less than the value of our
Target (rememeber, we already checked whether the current Node IS our target in the break condition).
If the current Node's value is less than our Target, then that necisarrily mean our Target lives on the
left subtree of our current Node. Else, it must exist in the right subtree. Coninue this process until Target
is found, then return. 

Note why we return the actual Node instead of just its value. The Node (return root) has the relationships of all
Nodes beneath it already attatched, as opposed to returning that Node's value, which would literally just be some 
number. This is why printTree() works the way it does (which does happen to use inorder traversal)
"""
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.val == target:
            return root
        
        if target < root.val:
            return self.searchBST(root.left, target)
        else:
            return self.searchBST(root.right, target)
        
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
