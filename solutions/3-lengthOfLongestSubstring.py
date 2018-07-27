'''
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating
characters.

Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the
    answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        max_len = 1
        i = 0
        j = 1
        d = {}
        d[s[i]] = i
        while i < len(s) and j < len(s):
            if s[j] in d and d[s[j]] >= i:
                max_len = max(max_len, j - i)
                i = d[s[j]] + 1
            else:
                max_len = max(max_len, j - i + 1)
            d[s[j]] = j
            j += 1
        return max_len
