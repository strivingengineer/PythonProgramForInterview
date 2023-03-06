maintainer = 'strivingengineer'
'''
Leetcode 409. Longest Palindrome
https://leetcode.com/problems/longest-palindrome/
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome 
that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.

Approach: We iterate over the string and store its character count in hashmap, the  we iterate over the hashmap values
and check if it is even then we can directly add it, if its odd then we can add value-1 in ans and only one add value 
can be added in the which we can handle through a Flag 
Time/Space: O(n)/O(n) 
'''


def longestPalindrome(s):
    res = {}

    for i in s:
        res[i] = res.get(i, 0) + 1
    ans = 0
    odd = True
    for value in res.values():
        if value % 2 == 0:
            ans += value
        elif odd:
            ans += value
            odd = False
        elif value > 1:
            ans += value - 1

    return ans

