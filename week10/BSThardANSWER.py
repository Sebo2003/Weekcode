"""
LEETCODE 450:
_______________________________________________________________________________________________________________
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the 
root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 
Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
Each node has a unique value.
root is a valid binary search tree.
-10^5 <= key <= 10^5
_______________________________________________________________________________________________________________
LOGIC:
_______________________________________________________________________________________________________________
This code builds off of the previous two problems, so read the logical explanation to the solution of those
problems before reading this one.

The first point of intrest is that our traversal method is different. Instead of stopping when root.val == x,
as in searching or insertion, we instead delegate the finding of our target value in the else statement
(If remove < root.val, go left. If remove > root.val, go right. If we are in a tree and our current root.val
is not less than or greater than remove, then that must mean our current root.val == remove!)

When we find our target node, we must then determine whether it has 0, 1, or 2 children, as that will change
how we rearrange our tree. The cases of 0 (Leaf) or 1 Children is covered by the contents of the Else, and the 
case of 2 Children is handled by the findSuccessor() function

if root.left is None: return root.right, elif root.right is None: return root.left. What does this mean?
Essentially if our current node (remember that root.val == remove is true if we are in this code block in
the first place) has no left child, return its right child. If it has no right child, return the left child.
Remember that in this point and time, we are at the very top of the recursive call stack. This is why we
are calling return in either case. Consider the following scenarios:

1) Our root has a right child, but no left child:
    Then, when we call return root.right, we are funneling this right child down the recursive call stack.
    In effect, this node replaces the node we were currently on, effectivley removing our target node from
    the tree while maintaing proper BST form

2) Our root has a left child, but no right child:
    Then, when we call return root.left, we are funneling this left child down the recursive call stack.
    In effect, this node replaces the node we were currently on, effectivley removing our target node from
    the tree while maintaing proper BST form

3) Our root has no left child or right child (it is a leaf):
    Then we are returning root.right (since the left child is checked first), which would be None. This
    None value is funneled down the recursive call stack, replacing the leaf node we were currently on.
    Effectivley, this removes that leaf while maintianing proper BST form

You'll see that this first condition covers whether our node-to-be-deleted has only 1 child or 0. But, if
that node had 2 children, neither of these if statements would be hit, and thus this block would fail. We
need a seperate case for when there are 2 children. After all, the fundamental logic of removing nodes is
swapping the values of parent and child, but when there are multiple children, which of the values do you
swap? Even worse, what if the child has children of its own, then what!?

We must assume that a child may have children to account for worst-case scenarios, so lets start there.
A property of BSTs is that all nodes of a root's right subtree will always be greater than the root itself.
Also, we know that in BSTs, for any individual parent, its left child will always be lesser than its right 
child. Finally, we know that in BST removal, any node that is deleted must be replaced with something (even
None in the case of Leaves). 

We need to maintain BST structure when removing (replacing) nodes from a tree. To achieve this, the node
we are removing should be replaced by the node whose value is immedialtey to the right of remove. In other
words, the next value in the tree greater than our target value. Where does that value exist? Well, since its
greater than our target, it lives in the right subtree. BUT, since its only the immediate next largest value,
its the "smallest of the largest". In other words, the leftmost node of the right subtree. Traditionally,
we call this node the "Inorder Successor", because if we were performing In-Order Traversal starting at the
node we are deleting, this node would be the next node to be encountered.

And so, in the case of the node-to-be-deleted having 2 children, we must replace it with its Inorder Successor,
which is the leftmost node of the right subtree. Simple enough then! We call findSuccessor(), which accepts
root.right as its paramater (the right subtree, essentially). findSuccessor() calls a while loop that continues
as long as a left node exist in this subtree. When the loop breaks, that means no more left nodes exists, so 
when it calls return node, it is returning the leftmost node in the right subtree. We save this value in
variable successor.

Then, we do: root.val = successor.val. In other words, we are replacing our root's value with its Inorder
Successor. So, are we done? If the children were all leaves, then yes. But, what if the children have
children of their own? This swapping could break the validity of BST, so how do we solve this problem? 
Well, simply find the Inorder Successor of the children's children. But what if the children's children
have children? Well then we'll find their Inorder Successor too. In fact, lets just recursivley go down the
entire subtree to make sure we have this base covered. 
Hence, we do: root.right = self.removeFromBST(root.right, successor.val)

Then, we return root, which will be the very top of our newly defined BST (the actual top of the BST, not
the top of the subtree we were just dealing with).

"""


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

        if remove < root.val:
            root.left = self.removeFromBST(root.left, remove)
        elif remove > root.val:
            root.right = self.removeFromBST(root.right, remove)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
        successor = self.findSuccessor(root.right)
        root.val = successor.val
        root.right = self.removeFromBST(root.right, successor.val)

        return root
    
    def findSuccessor(self, node: TreeNode) -> TreeNode:
        # Keep going left until reaching the leftmost node
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