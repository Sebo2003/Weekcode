"""
LEETCODE 701
_________________________________________________________________________________________________________________
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return 
the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the 
original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a
BST after insertion. You can return any of them.

Example 1:

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
 
Constraints:

The number of nodes in the tree will be in the range [0, 10^4].
-10^8 <= Node.val <= 10^8
All the values Node.val are unique.
-10^8 <= val <= 10^8
It's guaranteed that val does not exist in the original BST.
_________________________________________________________________________________________________________________
LOGIC:
_________________________________________________________________________________________________________________
This solution builds directly off of the easy answer's solution. So first read the Logic of that solution's
answer, then come back to this one. Because of this fact, the recursive logic will not be repeated here.

Note that, once again, we are doing a BFS search instead of pre/in/post order traversal. Really, the only
difference is our breaking condition. If we encoutner a Node that doesn't exit (if root == None), then
create one there, using our input insert (return TreeNode(insert)).

Remember that because of the recursive logic, once we encounter None, it is in the exact place where that
Node needs to be inserted. This is why we can simply state TreeNode(insert).
"""
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], insert: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(insert)
        
        if insert < root.val:
            root.left = self.insertIntoBST(root.left, insert)
        else:
            root.right = self.insertIntoBST(root.right, insert)
        
        return root

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

    insert = 5
    result = sol.insertIntoBST(root, insert)
    if result:
        print(sol.printTree(result))