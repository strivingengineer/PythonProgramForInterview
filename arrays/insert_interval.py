
maintainer = 'strivingengineer'

'''
57. Insert Interval
https://leetcode.com/problems/insert-interval/description/

You are given an array of non-overlapping intervals
 intervals where intervals[i] = [starti, endi] represent the start
  and the end of the ith interval and intervals is sorted in ascending 
  order by starti. You are also given an interval newInterval = [start, end] 
  that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in 
ascending order by starti and intervals still does not have any overlapping
 intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105

Approach 1:
Main idea is that when iterating over the intervals there are three cases:
1.the new interval is in the range of the other interval
2.the new interval's range is before the other
3.the new interval is after the range of other interval
'''
def insert(intervals, newInterval):
    if not intervals:
        return [newInterval]
    res =[]

    for i in range(len(intervals)):

        s, e = intervals[i]

        if newInterval[1] < s:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > e:
            res.append([s, e])
        else:
            newInterval = [min(newInterval[0], s), max(newInterval[1], e)]

    res.append(newInterval)

    return res

'''
Approach 2:Since the given intervals is already in sorted order, 
we can use binary search to find the insertion point. Then, merge the interval if necessary.
 
'''
import bisect


def insert(intervals, newInterval):
    i = bisect.bisect_left(intervals, newInterval)
    res = intervals[:i]
    for interval in [newInterval]+intervals[i:]:
        if res and res[-1][1] >= interval[0]:
            res[-1][1] = max(res[-1][1], interval[1])
        else:
            res.append(interval)
    return res

