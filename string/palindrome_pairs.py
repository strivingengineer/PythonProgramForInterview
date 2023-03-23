maintainer = 'strivingengineer'
'''
Leetcode 336. Palindrome Pairs
https://leetcode.com/problems/palindrome-pairs/
You are given a 0-indexed array of unique strings words.
A palindrome pair is a pair of integers (i, j) such that:
0 <= i, j < words.length,
i != j, and
words[i] + words[j] (the concatenation of the two strings) is a palindrome
Return an array of all the palindrome pairs of words.

Example 1:
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]

Example 2:
Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:
Input: words = ["a",""]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["a","a"]

Constraints:
1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lowercase English letters.

Approach:
we can iterate over all pairs of strings in the array and check if their concatenation is a palindrome. However, 
this approach has a time complexity of O(n^2 * m), where n is the number of strings in the array and m is the 
maximum length of the strings.

A more efficient approach is to use a hash table to store the indices of the strings in the array, and then 
iterate over all pairs of strings and check if their concatenation is a palindrome. We can also optimize the 
palindrome check by using a two-pointer approach.
Time/Space Complexity :O(n^2 * m)/O(n * m), where n is the number of strings in the input array and m is the maximum 
length of the strings 
'''


def palindromePairs(words):
    result = []
    word_indices = {word: i for i, word in enumerate(words)}

    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]

            if prefix == prefix[::-1]:
                reversed_suffix = suffix[::-1]
                if reversed_suffix != word and reversed_suffix in word_indices:
                    result.append([word_indices[reversed_suffix], i])

            if j != len(word) and suffix == suffix[::-1]:
                reversed_prefix = prefix[::-1]
                if reversed_prefix != word and reversed_prefix in word_indices:
                    result.append([i, word_indices[reversed_prefix]])

    return result


