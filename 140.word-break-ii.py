#
# @lc app=leetcode id=140 lang=python
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (27.33%)
# Likes:    970
# Dislikes: 252
# Total Accepted:    162.5K
# Total Submissions: 590K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
# 
#
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # sentences(i) returns a list of all sentences that can be built from the suffix s[i:]
        memo = {len(s): ['']}
        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail) for j in range(i + 1, len(s) + 1) if s[i:j] in wordDict for tail in sentences(j)]
            return memo[i]
        return sentences(0)

