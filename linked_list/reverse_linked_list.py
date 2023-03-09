maintainer = 'strivingengineer'
'''
Leetcode 206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/description/
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

Approach: Iterative: We can have couple of pointer to keep track of current , previous and current.next elements and
then removing the existing pointers and connect them to new direction
Time/Space complexity: O(n)/O(1) 
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: [ListNode]) :

        current, previous = head, None

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous


'''
Approach: Recursive: We have to track the base case until we hit the last node whose next is None and recursively 
pointing current.next to previous node
Time/Space Complexity: O(n)/O(1)
'''


def reverseListRecursive(head: [ListNode]):

    if not head:
        return None

    newhead = head

    if newhead.next:
        newhead = reverseListRecursive(head.next)
        head.next.next = head
    head.next = None

    return newhead

