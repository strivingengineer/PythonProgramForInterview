maintainer = 'strivingengineer'
'''
Leetcode 74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
Approach: We first find the row in the matrix in which our target element could be present then
we apply binary search to find the element if it exists or not in that row.
Time/Space: O(log(m*n)/O(1)
'''

def searchMatrix(matrix, target: int) -> bool:

        rowend = len(matrix)-1
        colend = len(matrix[0])-1

        rowstart,colstart=0,0

        if not matrix:
            return False
        row = -1
        while rowstart <= rowend:
            mid = (rowstart + rowend) // 2
            if matrix[mid][0] <= target <= matrix[mid][colend]:
                row = mid
                break
            elif matrix[mid][0] > target:
                rowend = mid - 1
            else:
                rowstart = mid + 1

        if row == -1:
            return False

        left, right = 0, colend
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

