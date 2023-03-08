maintainer = 'strivingengineer'
'''
Leetcode 21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/description/
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the 
nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

Approach: We will use dummy list to handle the edge cases.First you initialize dummy and temp. 
one is sitting at the start of the linkedlist & other (temp) is going to move forward find which 
value should be added to the list by checking which value is bigger out of two list and the moving the pointers for
temp, list1 and list2. Once we break the while loop, we check if we have elements in any of the lists, then add it in 
the end as its a sorted list.
Time/Space: O(m+n)/O(m+n)
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    #link to understand dummy node
    #https://stackoverflow.com/questions/58715870/explanation-about-dummy-nodes-and-pointers-in-linked-lists#:~:text=1%20Answer&text=dummy%20and%20cur%20both%20point,because%20it's%20the%20same%20list.&text=you're%20not%20creating%20a,pointer%20down%20the%20existing%20list
    dummy = ListNode()
    temp = dummy

    while list1 and list2:
        if list1.val < list2.val:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next

    if list1:
        temp.next = list1
    if list2:
        temp.next = list2

    return dummy.next

'''
Another approach is solving using recursion. Handle the base case of empty list.If one of them is empty, 
return the other one! Here, we have two cases, whatever list has the smaller first element, will be returned at the end 
Time/Space: O(m+n)/ Stack space of O(m+n)
'''


def mergeTwoLists(l1, l2):
    if not l1 or not l2:
        return l1 or l2

    if l1.val <= l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

