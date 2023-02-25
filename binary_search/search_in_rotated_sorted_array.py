maintainer = 'strivingengineer'
'''
Leetcode 33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is 
possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], 
nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be 
rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return 
the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

Approach: Since it is given the array is sorted and we have to solve the problem in log(n) time then we have to use 
binary search as these are the conditions of binary search.

So we know that our array is rotated so  directly we can not perform a Binary Search.
But if  nums[mid] is bigger than nums[left] we know the inflection(rotation) point will be to the right of us,
meaning values from nums[left] to  nums[mid] are ascending.
So if target is between that range we just cut our search space to the left. Otherwise go right.

The other condition is that nums[mid] is not bigger than nums[left] meaning nums[mid] to nums[right] is ascending.
In the same manner we can check if target is in that range and cut the search space correspondingly.
Time/Space complexity: O(log(n))/O(1)
'''


def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if target < nums[left] or target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1

    return -1

# recursive solution for problem
def search(nums, target):

    def helper(nums, target, start, end):

        mid = start + (end - start) // 2

        if start > end:
            return -1

        if nums[mid] == target:
            return mid

        elif nums[start] <= nums[mid]:
            if nums[start] <= target <= nums[mid]:
                return helper(nums, target, start, mid - 1)
            else:
                return helper(nums, target, mid + 1, end)
        else:
            if nums[mid] <= target <= nums[end]:
                return helper(nums, target, mid + 1, end)
            else:
                return helper(nums, target, start, mid - 1)

    return helper(nums, target, 0, len(nums) - 1)