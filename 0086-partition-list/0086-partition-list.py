# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        current = head
        small_num = ListNode(0)
        large_num = ListNode(0)

        small = small_num
        large = large_num
        while current:
            if current.val < x:
                small.next = current
                small = small.next
            else :
                large.next = current
                large = large.next
            current = current.next

        large.next = None
        small.next = large_num.next
        return small_num.next