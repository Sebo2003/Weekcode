"""
If you keep list1 = 1 -> 3 -> 5 -> 6, and list2 = 2 -> 3 -> 7, and your ouput is:
'1 2 3 3 5 6 7 '
then you know you've done it correctly 
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

class Solution:
    def mergeLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final_list = ListNode()
        
        #How do I make sure the the values of these two lists are inputted into the final_list linked list
        #in numerically increasing order, while also making sure each node in final_list actually points
        #to the next?

        #Example:
        #______________________
        #list1:   -1 -> 4 -> 5
        #list2:   0 -> 9
        #final_list:    -1 -> 0 -> 4 -> 5 -> 9
        #Notice how in final_list, each node correctly points to its neighbor

        return final_list.next

if __name__ == "__main__":
    sol = Solution()

    l1_values = [1, 3, 5, 6]
    l2_values = [2, 3, 7]

    l1 = create_linked_list(l1_values)
    l2 = create_linked_list(l2_values)

    merged_list = sol.mergeLists(l1, l2)

    while merged_list:
        print(merged_list.val, end=" ")
        merged_list = merged_list.next
