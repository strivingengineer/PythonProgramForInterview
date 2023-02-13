maintainer = 'strivingengineer'
'''
Leetcode 75. Sort Colors
https://leetcode.com/problems/sort-colors/
Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, 
white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

Approach 1: We can directly use the sorting method and solve the problem. 
Time : O(nlogn)/ O(1) or O(n) based on sorting algorithm 
'''


def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """

    nums.sort()  # Invalid solution since we are using inbuilt library function


'''
Another approach will be using three variable for counting the occurrence of each element and then
creating a array and then copying it to original array.
Time/Space: O(n)/O(1) space
'''


def sortColors(nums):
    red, white, blue = 0, 0, 0
    for i in nums:
        if i == 0:
            red += 1
        elif i == 1:
            white += 1
        else:
            blue += 1

    left, right = 0, len(nums) - 1

    while left <= right:
        while red > 0:
            nums[left] = 0
            left += 1
            red -= 1
        while white > 0:
            nums[left] = 1
            left += 1
            white -= 1
        while blue > 0:
            nums[left] = 2
            left += 1
            blue -= 1

'''
Another approach will be to swap the elements inplace based on its color value, 
Time/Space: O(n)/O(1)
'''


def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """

    left, mid, right = 0, 0, len(nums) - 1
    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1

