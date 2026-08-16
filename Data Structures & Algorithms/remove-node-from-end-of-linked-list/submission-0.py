# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find the total number of nodes through traversal
        curr = head
        total_cnt = 0
        while curr:
            curr = curr.next
            total_cnt += 1
        #find the index to remove the node of
        remove_index = total_cnt - n

        #edge case: if total count is 1, return Null
        if remove_index == 0:
            return head.next
        #traverse again with prev pointer, to skip over remove index
        
        curr = head
        for i in range(total_cnt-1):
            #update curr next to skip curr
            if (i+1) == remove_index:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head

        
            

        