maintainer = 'strivingengineer'
'''
Leetcode 239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/
You are given an array of integers nums, there is a sliding window of size k which is moving from the very 
left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window 
moves right by one position.
Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

Approach:
To solve this problem, we can use a deque (double-ended queue) to store the indices of the elements in the current 
window in descending order of their values.

At each step, we add the current element to the deque and remove the indices of elements that are smaller than the 
current element from the right end of the deque. We also remove the index of the first element in the deque if it is 
outside the current window. The maximum element in the current window is then the element at the front of the deque. 
We add this element to the result and repeat the process until we have processed all windows.

Time/Space Complexity: O(n)/O(k) where k is the size of the sliding window
'''

from collections import deque


def maxSlidingWindow(nums, k):
    if not nums:
        return []
    if k == 1:
        return nums

    n = len(nums)
    q = deque()
    result = []

    for i in range(k):
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(k, n):
        result.append(nums[q[0]])
        while q and q[0] <= i - k:
            q.popleft()
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)

    result.append(nums[q[0]])
    return result


'''
Another approach is to use a max heap to keep track of the maximum element in the current window. We can also use a 
deque to store the indices of the elements in the current window.

At each step, we add the index of the current element to the deque and remove the index of the first element in the 
deque if it is outside the current window. We then remove the indices of elements that are smaller than the current 
element from the right end of the deque. The maximum element in the current window is then the element at the front 
of the deque. We add this element to the result and repeat the process until we have processed all windows.
Time/Space Complexity: O(n log k)/O(k), which is the size of the heap
'''

import heapq

def maxSlidingWindow(nums, k):
    if not nums:
        return []
    if k == 1:
        return nums

    n = len(nums)
    q = []
    result = []

    for i in range(k):
        heapq.heappush(q, (-nums[i], i))

    result.append(-q[0][0])

    for i in range(k, n):
        heapq.heappush(q, (-nums[i], i))
        while q[0][1] <= i - k:
            heapq.heappop(q)
        result.append(-q[0][0])

    return result
