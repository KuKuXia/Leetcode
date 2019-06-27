#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.27%)
# Likes:    381
# Dislikes: 1609
# Total Accepted:    274.7K
# Total Submissions: 851.3K
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space
# characters only.
#
# Example:
#
#
# Input: "Hello World"
# Output: 5
#
#
#
#
#


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        # Slow and fast pointers
        slow = -1
        
        # Iterate over trailing spaces
        while slow >= -length and s[slow] == ' ':
            slow -= 1
        fast = slow
        
        # Iterate over last word
        while fast >= -length and s[fast] != ' ':
            fast -= 1
        return slow - fast


