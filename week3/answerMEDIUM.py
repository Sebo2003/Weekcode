"""
Leetcode 725:
_____________
Given the head of a singly linked list and an integer k, split the 
linked list into k consecutive linked list parts. The length of each part should 
be as equal as possible: no two parts should have a size differing by more than one. 
This may lead to some parts being null. The parts should be in the order of occurrence 
in the input list, and parts occurring earlier should always have a size greater than or 
equal to parts occurring later. Return an array of the k parts.

Example 1:

Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Example 2:

Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier 
parts are a larger size than the later parts.

Constraints:

    The number of nodes in the list is in the range [0, 1000].
    0 <= Node.val <= 1000
    1 <= k <= 50
_______________________________
Logic:

In order to solve this problem, we must first understand how to correctly split the list given integer k.
Since it is possible that k>n (where n is input size of the list), the smallest possible list that can exist
is a list of None, and the smallest list with elements is a list of one element [See Example 1]. 
Since each list must hav an identical amount of elements, and k>n can be true, in some instances, the linked 
lists at the front of the final array may be one element longer than the rest of the linked lists [See Example 2].

Thus, we can find the default size of any linked list as: length of header list integer divided by input k, or,
length // k. Likewise, we can find how many lists will have an extra node in them by finding the remainder of
the header list, or, length % k. We save both variables in def_size and extra_size, respectivley.

Now, instead of looping over the length of the head list, we iterate k times instead. Why? The reason is to
account for edge cases such as Example 1, where k>n. We do not want to stop just because we reached the end
of our input linked list, theoretically, we might need to go further beyond, up until k. Thus, we write
for i in range(k):

The idea is to iterate over the head linked list k times, splitting it every def_size or extra_size times. For
example, if we have an input of 10 (1,2,3,4,5,6,7,8,10) where k = 3, then we normally split the input every 3
elements, except the very first time where we split after 4 elements, because 10%3 = 1. Thus, we would have
(1,2,3,4)(5,6,7)(8,9,10). In this example, def_size = 3 (because 10//3 = 3), and extra_size = 1 (because 
10%3 = 1). Notice then, that we have 1 list of def_size+1 size, (1,2,3,4), and 2 of def_size, (5,6,7) & (8,9,10).
In code, once we reach the end of any of these sublists, we will make the final node point to None in order to
ensure these lists are indeed seperate from one another. In this example, 4 will point to None, 7 will point to
None, and 10 will point to None.

Given this, lets resume our loop. We left off at the very beginning of this process: for i in range(k):

Immediatley, we do returnList.append(curr). This is so we populate the currnet sublist that we are currently making.
Then, we do: sublist_size = def_size + (1 if i < extra_size else 0). We do this in order to find whether or not
our current sublist will have an extra node in it or not. Lets break it down further: def_size, the normal
size of any list, is the first part of this equation. Makes sense, since any linked list size will only ever
be one element larger than this value, or nothing at all. So, we continue. def_size + (1, why + 1? This is
the extra node that may or may not occur in this sublist. def_size + (1 if i < extra_size else 0), where
if i < extra_size else 0 is a pythonic unary operator. Bascially, its saying "only add this 1 if 
we have some lists that will have 1 extra node in them. And only do that so long as the number of lists like
this is less than our current iteration (this ensures the lists with extra nodes occur in the front of our
list). Else, add nothing at all (else 0)".

No matter if we're in a def_size or extra_size linked list, we continue with: for j in range(sublist_size - 1).
Why do we iterate sublist_size - 1 times? Its so we stop right before the node that points to None. Once this
loop is completed, curr will have moved all the way up until the node before the node that points to None.
Or, if we keep with our n=10,k=3 example, this loop will stop at elements 3, 6, and 9 respecitvley 
[(1,2,3,4)(5,6,7)(8,9,10)].

Now check if curr points to a node that points to None, we do this with: if curr:. If it is, then we continue
this if statement. This if statement can be condensed into three quick maneuvers:
1) temp = curr.next. We do this so a temporary pointer points to the next value of curr. So, if we're on 4, temp is pointing to 5.
2) curr.next = None. This is where we finally do the split. Now, curr.next points to nothing. So, if we're on 4, 4 is pointing to None
3) curr = temp. Now, we resume our iteration of k by setting curr to where temp is. So, if curr was on 4, now its on temp, which is on 5. 
Thus, we have split the list at tha appropriate place, and curr is now pointing to the head of the new sublist.

This process repeats until we iterate over all of k. At this point, because we did returnList.append(curr),
our returnList is full. So we simply return returnList, and the problem is solved. I also added a main function
so we could see what the printed result looks like.

This video helped me a lot too: https://www.youtube.com/watch?v=-OTlqdrxrVI
_______________________________
Steps:

1) Populate list with values 0 through size
2) Call splitListToParts() with list & k
3) Get length of list
4) Find how many linked lists will have the normal amount of elements
5) Find how many linked lists will have 1 extra element in them
6) Iterate over head list k amount of times
7) Add the current node to the list
8) Determine if the current sublist needs an extra node or not
9) Iterate until [(end of sublist) - 1] times (as to account for the next node pointing to None)
10) Determine wether the next node points at None or not. If it doesn't, then continue
11) Once we reach the end of the sublist, set a temprorary curosor node to the next node after the current one. 
    Set the next node as None, to signify the end of the sublist. Then, reestablish the curosor pointer to temp,
    as to begin iteration for the next sublist
12) Return the list, so that it may be printed in main
"""
import sys
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def generateList(self, size: int) -> Optional[ListNode]: #step 1 elaborated
        if size <= 0:
            print("Size is not supposed to be <= 0")
            sys.exit(1)
            
        dummy = ListNode() 
        current = dummy
        for i in range(size):
            current.next = ListNode(i+1)  
            current = current.next

        current = dummy.next
        print("init: ", end=" ")
        while current:
            print(current.val, end=" ")
            current = current.next  
        print()

        return dummy.next

    def splitListToParts(self, head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
        returnList = []
        length = 0
        curr = head
        while curr: #step 3
            curr = curr.next
            length+=1
        
        #print("n = ", length)
        def_size = length//k #step 4
        #print("base size: ", def_size)
        extra_size = length%k #step 5
        #print("# of linked lists with extra node: ", extra_size)

        curr = head
        for i in range(k): #step 6
            returnList.append(curr) #step 7
            sublist_size = def_size + (1 if i < extra_size else 0) #step 8
            for j in range(sublist_size - 1): #step 9
                if curr: #step 10
                    curr = curr.next 
            if curr: #step 11
                temp = curr.next
                curr.next = None
                curr = temp
        
        return returnList #step 12

if __name__ == "__main__":
    sol = Solution()

    l1 = sol.generateList(3) #step 1
    k = 5
    finalh = sol.splitListToParts(l1, k) #step 2

    print("final:", end=" ")
    print("[", end=" ")
    for sublist in finalh:
        if sublist:
            current = sublist
            print("[", end=" ")
            while current:
                print(current.val, end=", ")
                current = current.next
            print("\b\b]", end=" ")
        else:
            print("[]", end=" ")
    print("]", end=" ")
