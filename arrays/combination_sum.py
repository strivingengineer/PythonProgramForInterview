maintainer = 'strivingengineer'
'''
Leetcode- 39. Combination Sum
https://leetcode.com/problems/combination-sum/description/
Given an array of distinct integers candidates and a target integer target, return a list of all 
unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to 
target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40


Approach 1: Use backtracking and try to form every combination using dfs function.
cur: current combination, cur_sum current combination sum, current index i (to avoid repeats)
Time complexity: O(N^M), N = len(candidates), M = target
Space complexity: O(M)
'''


def combinationSum(candidates: list, target: int) -> list:
    res = []
    n = len(candidates)

    def dfs(cur, cur_sum, index):  # try out each possible cases
        if cur_sum > target:
            return  # this is the case, cur_sum will never equal to target
        if cur_sum == target:
            res.append(cur)
            return  # if equal, add to `ans`
        for i in range(index, n):
            dfs(cur + [candidates[i]], cur_sum + candidates[i], i)

    dfs([], 0, 0)
    return res

'''
Another approach to solve the problem using dfs 
Time Complexity: O(N^M), N = len(candidates), M = target
Space Complexity: O(M)
'''

def combinationSum(candidates: list, target: int) -> list:
    res = []

    def dfs(i, cur, total):

        if total == target:
            res.append(cur.copy())
            return

        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res


'''
This is dp solution to compute the combination sum
Time Complexity: O(M*M*N), N = len(candidates), M = target
Space Complexity: O(M*M)
'''

def combinationSum(candidates: list, target: int) -> list:
    dp = [[] for _ in range(target + 1)]
    for c in candidates:  # O(N): for each candidate
        for i in range(c, target + 1):  # O(M): for each possible value <= target
            if i == c:
                dp[i].append([c])
            for comb in dp[i - c]:
                dp[i].append(comb + [c])  # O(M) worst: for each combination
    return dp[-1]
