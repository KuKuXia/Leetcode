#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (50.07%)
# Likes:    1039
# Dislikes: 79
# Total Accepted:    279.5K
# Total Submissions: 556.5K
# Testcase Example:  '"leetcode"'
#
#
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
# Note: You may assume the string contain only lowercase letters.
#
#


class Solution(object):
    def firstUniqChar_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        dict_num = {}
        idx, ret = 0,-1
        for i in range(len(s)):
            dict_num[s[i]] = dict_num.setdefault(s[i], 0) + 1

        for i in range(len(s)):
            a = dict_num.get(s[i])
            if a == 1:
                ret = idx
                break
            idx += 1
        return ret
    
    def firstUniqChar(self, s):
        d = {c: s.count(c) for c in set(s)}
        return ([i for i, c in enumerate(s) if d[c]==1] + [-1])[0]
