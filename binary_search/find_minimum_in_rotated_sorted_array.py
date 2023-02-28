maintainer = 'strivingengineer'
'''
Leetcode 153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Suppose an array of length n sorted in ascending order is rotated between 
1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.

Approach: Since we have to solve the problem in Log(n) time then only thing we have to do is the use of binary search.

Time/Space: O(log(n))/O(1)
'''

def findMin(nums):

    ans = nums[0]
    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] < nums[right]:
            ans = min(ans, nums[left])
            break

        mid = left + (right - left) // 2
        ans = min(ans, nums[mid])
        if nums[mid] >= nums[left]:
            left = mid +1
        else:
            right = mid -1

    return ans

'''
Another approach can be we have to check if mid is greater than right then we change the left pointer else
make right equal to mid so that we stay in loop until our condition break and finally the left will be on the minimum
value.
Time/Space: O(log(n))/O(1)
'''

def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid
    return nums[left]

