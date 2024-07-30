# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head_palindrome = []
        
        pointer = head
        while pointer is not None:
            head_palindrome.append(pointer.val)
            pointer = pointer.next
            
        if head_palindrome == head_palindrome[::-1]:
            return True
        else:
            return False
            
        