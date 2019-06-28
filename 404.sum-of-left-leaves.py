#
# @lc app=leetcode id=404 lang=python
#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (49.12%)
# Likes:    674
# Dislikes: 79
# Total Accepted:    129.1K
# Total Submissions: 262.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Find the sum of all left leaves in a given binary tree.
# 
# Example:
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15
# respectively. Return 24.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if not root else (root.left.val if root.left and not(root.left.left or root.left.right) else 0) + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

