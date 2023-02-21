maintainer = 'strivingengineer'
'''
Leetcode 128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109

Approach: Simple is we use sort the input list check if we have consecutive numbers or not. Time O(nlogn) but the
problem wants us to solve it in O(n) so we have to do better.
Now we can create a set of unique number and then check for every number the sequence will start if that number-1
is not present in set and we have to check till how long the sequence will present in set.
Time/Space: O(n)/O(n)
'''


def longestConsecutive(nums):
    values = set(nums)
    ans = 0
    for value in nums:

        if value - 1 not in values:  # check starting of new sequence
            currentlength = 0
            while value + currentlength in values: # check how long we have current sequence
                currentlength += 1
            ans = max(ans, currentlength)

    return ans

