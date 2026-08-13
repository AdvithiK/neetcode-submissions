# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #cycle detection, two pointers: slow & fast
        s = head
        f = head

        #check f and f.next isn't null
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        #if there's an exit null, theres no cycle
        return False

        