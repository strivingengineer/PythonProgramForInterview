maintainer = 'strivingengineer'
'''
Leetcode 5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
Approach:
Create a two-dimensional array dp of size n x n, where n is the length of the string s.
Each cell dp[i][j] represents whether the substring s[i:j+1] is a palindrome or not.
Initialize all the diagonal elements of dp to true, as a string of length 1 is always a palindrome.
For each substring s[i:j+1], check if s[i] is equal to s[j], and if dp[i+1][j-1] is true. If both 
conditions are satisfied, then dp[i][j] is also true, since s[i:j+1] is a palindrome. Otherwise, dp[i][j] is false.
While filling up the dp array, keep track of the longest palindrome substring seen so far.
Once the dp array is filled up, return the longest palindrome substring.

Time/Space complexity: O(n^2)/(n^2)
'''


def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    longest_palindrome = ""

    # Base case - all substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True
        longest_palindrome = s[i]

    # Check for palindromes of length 2 and above
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j] and (l == 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if len(s[i:j + 1]) > len(longest_palindrome):
                    longest_palindrome = s[i:j + 1]

    return longest_palindrome

'''
Another approach is using Manacher's algorithm.
The basic idea of Manacher's algorithm is to use symmetry to avoid re-evaluating palindromic substrings that have 
already been processed. The algorithm keeps track of the rightmost palindrome seen so far,
and uses its symmetry to determine the palindromes around it.

Time/Space complexity: O(n)/(n)
'''


def longest_palindromic_substring(s):
    # Transform input string s to an odd length string to simplify handling of even length palindromes
    n = len(s)
    new_s = '#' + '#'.join(s) + '#'
    n_new = len(new_s)

    # Initialize variables
    p = [0] * n_new
    center = right = 0
    max_len = max_center = 0

    # Loop through the transformed string to find the longest palindrome
    for i in range(n_new):
        if i < right:
            p[i] = min(right - i, p[2 * center - i])
        else:
            p[i] = 1

        # Try to expand palindrome centered at i
        while i - p[i] >= 0 and i + p[i] < n_new and new_s[i - p[i]] == new_s[i + p[i]]:
            p[i] += 1

        # Update center and right if palindrome centered at i expands beyond right
        if i + p[i] > right:
            center, right = i, i + p[i]

        # Update max_len and max_center if necessary
        if p[i] > max_len:
            max_len = p[i]
            max_center = i

    # Get the longest palindromic substring from max_center and max_len
    longest_palindrome = new_s[max_center - max_len + 1:max_center + max_len].replace('#', '')

    return longest_palindrome
