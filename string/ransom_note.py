maintainer = 'strivingengineer'
'''
Leetcode 383. Ransom Note
https://leetcode.com/problems/ransom-note/description/
Given two strings ransomNote and magazine, return true if ransomNote can be 
constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

Approach: We should traverse and store characters of magazine in a hashmap with its count as values and iterate over 
characters of ransomNote by checking if its value exists in hashmap and its count is greater than zero, else return 
False.
Time/Space Complexity: O(n)/O(n)
'''


def canConstruct(ransomNote, magazine):
    if len(ransomNote) > len(magazine):
        return False

    res = {}

    for i in magazine:
        res[i] = res.get(i, 0) + 1

    for j in ransomNote:
        if j not in res or res[j] <= 0:
            return False

        if j in res:
            res[j] -= 1

    return True

