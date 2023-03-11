maintainer = 'strivingengineer'
'''
Leetcode 14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/description/
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

Approach: We can iterate over the length of first word in the list and check with all other words till how long
it has same characters in it, if starting character of new word is not same then we can immediately return False
Time/Space: O(n)/ O(len(firstword))
'''

def longestCommonPrefix(strs):

    ans = ''

    for i in range(len(strs[0])):
        for word in strs[1:]:

            if i == len(word) or strs[0][i] != word[i]:
                return ans
            else:
                ans += strs[0][i]

    return ans

