maintainer = 'strivingengineer'
'''
Leetcode 49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

Approach: we use a dictionary to store the anagrams. For each string in the input array, we sort its characters 
and use the sorted string as a key in the dictionary. We then add the original string to the list of anagrams 
corresponding to its key. Finally, we return a list of the anagram lists from the dictionary.
Time/Space Complexity: O(nklog(k)) where n is the number of strings in the array, and k is the maximum length of a 
string/ O(n*k) where the keys are strings of length k, and the values are lists of strings
'''


def groupAnagrams(strs):
    # create a dictionary to store the anagrams
    anagrams = {}

    # iterate through each string in the array
    for s in strs:
        # sort the characters of the string to create a key
        key = ''.join(sorted(s))

        # add the string to the dictionary with the key
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]

    # return the list of anagrams
    return list(anagrams.values())

'''
we use a hash table to store the anagrams. For each string in the input array, we create a key by counting the 
frequency of each character in the string. We then convert the list of counts to a tuple and use it as a key in the 
dictionary. We add the original string to the list of anagrams corresponding to its key. Finally, we return a 
list of the anagram lists from the dictionary.
Time complexity of this solution is O(nk), where n is the number of strings in the array and k is the maximum length 
of a string. 
The space complexity is also O(nk), as we need to store a dictionary where the keys are tuples of length 26, 
and the values are lists of strings
'''


def groupAnagrams(strs):
    # create a dictionary to store the anagrams
    anagrams = {}

    # iterate through each string in the array
    for s in strs:
        # initialize a list for the anagrams of the current string
        key = [0] * 26
        for c in s:
            # increment the count of the current character in the key
            key[ord(c) - ord('a')] += 1

        # add the string to the dictionary with the key
        key = tuple(key)
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]

    # return the list of anagrams
    return list(anagrams.values())

