#
# @lc app=leetcode id=226 lang=python
#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (58.25%)
# Likes:    1764
# Dislikes: 28
# Total Accepted:    334K
# Total Submissions: 570.5K
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# Invert a binary tree.
#
# Example:
#
# Input:
#
#
# ⁠    4
# ⁠  /   \
# ⁠ 2     7
# ⁠/ \   / \
# 1   3 6   9
#
# Output:
#
#
# ⁠    4
# ⁠  /   \
# ⁠ 7     2
# ⁠/ \   / \
# 9   6 3   1
#
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew), but you
# can’t invert a binary tree on a whiteboard so f*** off.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def invertTree_1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = self.invertTree(
                root.right), self.invertTree(root.left)
        return root

    def invertTree_2(self, root):
        if root:
            invert = self.invertTree_1
            root.left, root.right = invert(root.right), invert(root.left)
        return root

    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                # the order is not matter
                stack += node.right, node.left
        return root
