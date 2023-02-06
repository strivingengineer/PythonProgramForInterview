maintainer = 'strivingengineer'

'''
Leetcode- 217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/

Given an integer array nums, return true if any 
value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109

Approach 1: We can compare the length of input list with a set value of same list and return based on 
len(input_list)!= len(set(input_list))
Time Space: O(n)/O(n)
'''


def containsDuplicate(nums):
    return len(nums) != len(set(nums))


'''
Another approach will be to use a hashmap/hashset to store already visited elements and check if current
element is present in  hashmap/hashset  if yes return True.
'''


def containsDuplicate(nums):
    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)

    return False
