maintainer = 'strivingengineer'
'''
Leetcode 76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?

Approach:
1.Initialize two dictionaries: one for the character frequencies of t, and one for the current window in s.
2.Use two pointers, left and right, to define the current window in s. Initialize both pointers to 0.
3.While the window doesn't contain all the characters in t, expand the window to the right by moving the right 
pointer and updating the frequency of the characters in the window dictionary.
4.Once the window contains all the characters in t, start shrinking the window from the left end by moving 
the left pointer and updating the frequency of the characters in the window dictionary.
5.At each step of shrinking the window, check if the window still contains all the characters in t. 
If not, go back to step 3 and continue expanding the window.
6.Keep track of the minimum window found so far.
7.Once the window no longer contains all the characters in t, return the minimum window found.
Time/Space Complexity: O(m + n)/ O(n)
'''


def minWindow(s: str, t: str) -> str:
    t_freq = {}
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1
    window_freq = {}

    # Step 2: Initialize pointers
    left = right = 0

    # Step 3: Expand window
    min_window = ""
    while right < len(s):
        if s[right] in t_freq:
            window_freq[s[right]] = window_freq.get(s[right], 0) + 1
        while all(freq <= window_freq.get(char, 0) for char, freq in t_freq.items()):
            # Step 4: Shrink window
            if not min_window or right - left < len(min_window):
                min_window = s[left:right + 1]
            if s[left] in t_freq:
                window_freq[s[left]] -= 1
            left += 1
        right += 1

    # Step 7: Return result
    return min_window if min_window else ""

