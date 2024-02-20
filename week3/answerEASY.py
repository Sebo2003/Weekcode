#Leetcode 21

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
        dummy = final_list

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next

        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2

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
