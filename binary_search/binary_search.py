maintainer = 'strivingengineer'

'''
Leetcode- 704. Binary Search
https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

Approach 1: Iterative : We have to take two pointers , one pointing to the start of array and another at the 
last index of list. then iterate over the list by comparing the value present at the mid = low + (high-low)//2,
if the value at mid is greater than target value, change start pointer to mid+1 , if its less than mid then 
change the end pointer to mid-1. If it is equal to value at mid index return index
'''


def binarySearch1(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            return mid

    return -1

'''
Another approach will be recursive approach which start and end of search also as input and then we check if
start pointer is greater than end pointer then we return -1.
Else we check if mid index is having target value or not if yes return index else reduce the search space to left
side or right side of mid based on whether mid index value is greater or lesser than target value.
'''

def binarySearch(nums, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if target == nums[mid]:
        return mid
    elif target > nums[mid]:
        return binarySearch(nums,target,mid+1, high)
    else:
        return binarySearch(nums, target, low, mid - 1)
