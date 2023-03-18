maintainer = 'strivingengineer'
'''
Leetcode 438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may 
return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
Approach: 
We first create a frequency table of all the characters in string p. Then, we create another frequency table for the
first substring of s with the same length as p. We then slide the window to the right by one character at a time 
and update the frequency table accordingly. If the frequency tables match, we have found an anagram and add its 
starting index to the result.
Time/Space Complexity: O(n)/O(1)
'''

def findAnagrams(s, p):
    freq_p = [0] * 26
    freq_s = [0] * 26
    res = []

    if len(s) < len(p):
        return res

    # Create frequency table for p
    for c in p:
        freq_p[ord(c) - ord('a')] += 1

    # Create frequency table for first substring of s
    for i in range(len(p)):
        freq_s[ord(s[i]) - ord('a')] += 1

    # Slide the window and check for anagrams
    for i in range(len(p), len(s)):
        if freq_p == freq_s:
            res.append(i - len(p))

        # Update frequency table for sliding window
        freq_s[ord(s[i]) - ord('a')] += 1
        freq_s[ord(s[i - len(p)]) - ord('a')] -= 1

    # Check last substring
    if freq_p == freq_s:
        res.append(len(s) - len(p))

    return res

'''
We can create two hash tables, one for the pattern string p and another for the sliding window substring of s.
The hash table will store the frequency of characters in each string.
Time/Space Complexity: O(n)/O(k) where k is the number of distinct characters in pattern string p
'''


def findAnagrams(s, p):
    res = []
    p_len = len(p)
    s_len = len(s)
    if s_len < p_len:
        return res

    p_freq = {}
    s_freq = {}

    # Create frequency table for pattern p
    for c in p:
        if c not in p_freq:
            p_freq[c] = 1
        else:
            p_freq[c] += 1

    # Create frequency table for first substring of s
    for i in range(p_len):
        c = s[i]
        if c not in s_freq:
            s_freq[c] = 1
        else:
            s_freq[c] += 1

    # Slide the window and check for anagrams
    for i in range(p_len, s_len):
        if p_freq == s_freq:
            res.append(i - p_len)

        # Update frequency table for sliding window
        left_char = s[i - p_len]
        if s_freq[left_char] == 1:
            del s_freq[left_char]
        else:
            s_freq[left_char] -= 1

        right_char = s[i]
        if right_char not in s_freq:
            s_freq[right_char] = 1
        else:
            s_freq[right_char] += 1

    # Check last substring
    if p_freq == s_freq:
        res.append(s_len - p_len)

    return res

