"""
If you keep n = 10 and k = 3, which it already is in this boilerplate, and you return with
'final: [ [ 1, 2, 3, 4] [ 5, 6, 7] [ 8, 9, 10] ] ',
then you know you've done it right. Likewise, if you do n = 3 and k = 5, and it returns with 
'final: [ [ 1] [ 2] [ 3] [] [] ]'
thats also correct
"""
import sys
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def generateList(self, size: int) -> Optional[ListNode]: 
        dummy = ListNode()
        if size <= 0:
            print("Size is not supposed to be =<0")
            sys.exit(1)

        #how would I generate a linked list, when I'm given a size as a parameter? 
        #if size = 5, my linked list should be: 1 -> 2 -> 3 -> 4 -> 5
        
        #Optional, but helpful:
        #_______________________________________
        #Since this function generates the linked list, I can also use it to print each node
        #of the linked list, just to make sure its initially correct before I begin modyfing it.
        #How would I print each value in the linked list?
            
        return dummy.next

    def splitListToParts(self, head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
        returnList = []

        #how would I split these linked lists, and put them into the returnList in the correct order, 
        #when I'm given head and k as a parameter?
        
        return returnList 
    
if __name__ == "__main__":
    sol = Solution()

    l1 = sol.generateList(10) #input whatever you want. For n=10, this will make a linked list of 1 -> 2 -> 3 ... -> 10
    k = 3 #Change k to whatever you want. 
    finalh = sol.splitListToParts(l1, k) 

    #print my list of linked lists
    print("final:", end=" ")
    print("[", end=" ")
    for sublist in finalh:
        current = sublist
        print("[", end=" ")
        while current:
            print(current.val, end=", ")
            current = current.next
        print("\b\b]", end=" ")
    print("]", end=" ")