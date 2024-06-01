# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head!=None:
            arr.append(head.val)
            head = head.next
        for i in range(len(arr)):
            if i > (len(arr)-1-i):
                return True
            if arr[i] != arr[len(arr)-1-i]:
                return False
        return True