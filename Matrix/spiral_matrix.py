maintainer = 'strivingengineer'
'''
54. Spiral Matrix
https://leetcode.com/problems/spiral-matrix/description/
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

Approach:To traverse an m x n matrix in spiral order, we can use a four-step process. Starting at the top-left 
corner of the matrix, we move right until we hit the end of the row, then down until we hit the bottom of the 
column, then left until we hit the beginning of the row, then up until we hit the top of the column. We repeat 
these four steps until we have traversed the entire matrix in a spiral order.
Time/Space Complexity: O(m*n), where m is the number of rows and n is the number of columns in the matrix/ 
O(mn), as the resulting list of elements visited in spiral order will contain mn elements in the worst case
'''

def spiralOrder(matrix):
    result = []
    if not matrix:
        return result

    # Define the boundaries of the matrix
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

'''
One approach is to use a direction matrix that keeps track of the direction in which we should move next. We start 
by moving to the right, then down, then left, then up, and repeat until we have visited all elements in the matrix.
Time/Space Complexity:O(mn), where m is the number of rows and n is the number of columns in the matrix./O(m*n)
'''

def spiralOrder(matrix):
    result = []
    if not matrix:
        return result

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_idx = 0
    m, n = len(matrix), len(matrix[0])
    row, col = 0, 0

    for i in range(m * n):
        result.append(matrix[row][col])
        matrix[row][col] = None

        next_row, next_col = row + directions[direction_idx][0], col + directions[direction_idx][1]
        if 0 <= next_row < m and 0 <= next_col < n and matrix[next_row][next_col] is not None:
            row, col = next_row, next_col
        else:
            direction_idx = (direction_idx + 1) % 4
            row, col = row + directions[direction_idx][0], col + directions[direction_idx][1]

    return result

'''
use a recursive function that visits each layer of the matrix in spiral order. The function takes as input the 
matrix, the starting row index, the ending row index, the starting column index, and the ending column index. 
It appends each element in the current layer to the result list, and then calls itself recursively with the 
indices adjusted to the next layer.
Time/Space Complexity:O(mn), where m is the number of rows and n is the number of columns in the matrix./O(m*n)
'''

def spiralOrder(matrix):
    result = []
    if not matrix:
        return result

    def traverse_layer(matrix, start_row, end_row, start_col, end_col):
        if start_row > end_row or start_col > end_col:
            return

        # Traverse right
        for col in range(start_col, end_col + 1):
            result.append(matrix[start_row][col])

        # Traverse down
        for row in range(start_row + 1, end_row + 1):
            result.append(matrix[row][end_col])

        # Traverse left (if applicable)
        if start_row < end_row:
            for col in range(end_col - 1, start_col - 1, -1):
                result.append(matrix[end_row][col])

        # Traverse up (if applicable)
        if start_col < end_col:
            for row in range(end_row - 1, start_row, -1):
                result.append(matrix[row][start_col])

        # Recursively traverse the next layer
        traverse_layer(matrix, start_row + 1, end_row - 1, start_col + 1, end_col - 1)

    traverse_layer(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1)
    return result



