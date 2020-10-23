'''
Description: 
Author: chen
Date: 2020-10-23 21:54:04
LastEditTime: 2020-10-23 22:06:14
LastEditors: chen
FilePath: /algorithm018/week01/homework/leetcode_21.py
'''
#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (64.54%)
# Likes:    1341
# Dislikes: 0
# Total Accepted:    395.2K
# Total Submissions: 612.1K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 递归合并
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        1.终止条件: l1空返回l2
                    l2空返回l1
        2.递归调用:
                l1.data>l2.data  l1.next = self.mergeTwoLists(l1.next,l2) return l1 
                l1.data<=l2.data  l2.next = self.mergeTwoLists(l2.next,l1)  return l2 
        """
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2


# @lc code=end

