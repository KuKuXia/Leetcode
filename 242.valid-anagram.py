#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (52.21%)
# Likes:    732
# Dislikes: 109
# Total Accepted:    352.3K
# Total Submissions: 670.7K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
#
# Example 1:
#
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
#
#


class Solution(object):
    def isAnagram_1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict_s = {}
        for key in s:
            dict_s[key] = dict_s.get(key, 0) + 1
        dict_t = {}
        for key in t:
            dict_t[key] = dict_t.get(key, 0) + 1
        return dict_s == dict_t

    def isAnagram_2(self, s, t):
        return sorted(s) == sorted(t)
    
    def isAnagram(self, s, t):
        dict_s, dict_t = [0] * 26, [0] * 26
        for key in s:
            dict_s[ord(key) - ord('a')] += 1
        for key in t:
            dict_t[ord(key) - ord('a')] += 1
        return dict_s == dict_t
