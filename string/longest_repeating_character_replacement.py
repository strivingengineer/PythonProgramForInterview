maintainer = 'strivingengineer'
'''
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of the string and change it to any 
other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above 
operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

Approach:

We can start by initializing two pointers, left and right, at the beginning of the string s. We can also initialize 
a dictionary, freq, to keep track of the frequency of each character in the current window. Then we can move the 
right pointer to the right until we reach a point where changing any character in the current window would require 
more than k changes. At this point, we can update the maximum length of the longest substring containing the same 
character, and move the left pointer to the right until we can make changes to the window again. We can repeat this 
process until we reach the end of the string s.
Time/Space Complexity: O(n)/O(26+k), where 26 is the number of uppercase English characters and k is the maximum number 
of allowed changes
'''


def characterReplacement(s: str, k: int) -> int:
    left = 0
    freq = {}
    max_len = 0
    max_freq = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        max_freq = max(max_freq, freq[s[right]])
        if right - left + 1 - max_freq > k:
            freq[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

'''
we can maintain a count of the frequency of each character in the entire string s using an array or dictionary. 
Then, we can use two pointers, left and right, to traverse the string s and keep track of the maximum length of 
the longest substring containing the same character that can be obtained by changing at most k characters.
Time/Space Complexity: O(n)/O(1)
'''

def characterReplacement(s: str, k: int) -> int:
    counts = [0] * 26
    left = right = max_count = 0
    for right in range(len(s)):
        counts[ord(s[right]) - ord('A')] += 1
        max_count = max(max_count, counts[ord(s[right]) - ord('A')])
        if right - left + 1 - max_count > k:
            counts[ord(s[left]) - ord('A')] -= 1
            left += 1
    return right - left + 1

