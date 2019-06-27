#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
#
# algorithms
# Easy (49.45%)
# Likes:    75
# Dislikes: 28
# Total Accepted:    6.3K
# Total Submissions: 11.9K
# Testcase Example:  '"ABCABC"\n"ABC"'
#
# For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T
# concatenated with itself 1 or more times)
# 
# Return the largest string X such that X divides str1 and X divides str2.
# 
# 
# 
# Example 1:
# 
# 
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# 
# 
# Example 2:
# 
# 
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1[i] and str2[i] are English uppercase letters.
# 
#
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        while str2:
            
            a = len(str1) % len(str2)
            n = len(str1) // len(str2)

            if a == 0 and str1 != str2 * n or a > 0 and str1[:-a] != str2 * n:
                return ''
                     
            if a == 0:
                return str2
            
            str1, str2 = str2, str1[-a:]
        return str2

