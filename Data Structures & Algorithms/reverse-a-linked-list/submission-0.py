# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #set previous pointer & current pointer
        prev, curr = None, head
        #while list is not empty,  no need for edge case
        while curr:
            #store the curr.next in temp
            temp = curr.next
            #switch the curr.next pointer to point at prev
            curr.next = prev
            #get prev to where curr is at
            prev = curr
            #change curr to where temp is at
            curr = temp
        #prev is at the last of the list, now, will point backwards
        return prev


        