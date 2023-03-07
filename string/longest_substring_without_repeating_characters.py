maintainer = 'strivingengineer'
'''
Leetcode 3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Approach: We will use sliding windows algorithm for solving the problem.
We can have use a set to already visited characters and two pointers to track the elements present in set and current 
element of string and if we encounter current element already present in set then we pop from set and add current
character in set and we compute the res variable every time we add element in set and return it in the end.
Time/Space: O(n)/O(n)
'''

def lengthOfLongestSubstring(s):
    res = 0
    seen = set()
    i, j = 0, 0
    while i < len(s):
        while s[i] in seen:
            seen.remove(s[j])
            j += 1
        seen.add(s[i])
        res = max(res, i-j+1)
        i += 1

    return res

