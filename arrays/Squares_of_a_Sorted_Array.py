maintainer = 'strivingengineer'

'''
Leetcode: 977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Simplest approach will to use inbuilt sorted function:

It will be  O(nlogn)/O(1) since we are not using extra memory 
'''


def sortedSquares(nums):
    return sorted([i * i for i in nums])

'''
Another approach would be to use a two pointer approach in which we will iterate over the array using
two pointers and check if the square of left side or right side is greater, then put the result from reverse side
this will be a O(n) approach.
'''


def sortedSquares(nums):
    res = [-1] * len(nums)

    i, j = 0, len(nums) - 1
    k = len(nums) - 1

    while i <= j:
        if nums[i] * nums[i] > nums[j] * nums[j]:
            res[k] = nums[i] * nums[i]
            i += 1
        else:
            res[k] = nums[j] * nums[j]
            j -= 1
        k -= 1

    return res