maintainer = 'strivingengineer'

'''
Leetcode- 283. Move Zeroes
https://leetcode.com/problems/move-zeroes/description/

Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 
Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 
Follow up: Could you minimize the total number of operations done?

Approach 1: We traverse through the array and in encounter any zero ,
we store it in zero array and if we encounter nonzero element then store it in non zero array and 
return the combination of both.
This approach will have O(n) time /O(n)space complexity 

'''

def move_zero1(nums):
    zero_list =[]
    nonzero_list= []

    for i in nums:
        if i == 0:
            zero_list.append(i)
        else:
            nonzero_list.append(i)

    return nonzero_list+zero_list

'''
Another better approach will be to use two pointer which saves us extra memory.
have two pointers both initialized to zero and iterate over the array and check it current element is non-zero,
if yes swap current element and element present in another pointer place
'''

def move_zero(nums):
    l, r = 0, 0

    while r < len(nums):
        if nums[r] != 0:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
        r += 1

    return nums
