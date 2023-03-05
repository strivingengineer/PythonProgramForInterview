maintainer = 'strivingengineer'
'''
Leetcode 242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or 
phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

Approach: We can use the a hashmap to store the values in it for string 1 and iterate over the string2 by checking if 
the value of current character is greater than 0 in hashmap , if not return False
Time/Space Complexity: O(n)/O(n)
'''

from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)

def isAnagram(s, t):
    return sorted(s) == sorted(t)

def isAnagram(s, t):
    res = {}

    if len(s) != len(t):
        return False

    for i in s:
        res[i] = res.get(i, 0)+1

    for c in t:
        if c not in res or res[c] <= 0:
            return False
        res[c] -= 1

    return True


