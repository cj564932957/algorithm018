'''
Description: 
Author: chen
Date: 2020-10-23 22:07:12
LastEditTime: 2020-10-23 22:48:11
LastEditors: chen
FilePath: /algorithm018/week01/homework/leetcode_88.py
'''
from typing import List
#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (48.80%)
# Likes:    670
# Dislikes: 0
# Total Accepted:    222.2K
# Total Submissions: 455.3K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
#
#
# 说明：
#
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
#
#
#
# 示例：
#
#
# 输入：
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出：[1,2,2,3,5,6]
#
#
#
# 提示：
#
#
# -10^9
# nums1.length == m + n
# nums2.length == n
#
#
#

# @lc code=start


class Solution:
    # 合并 再排序
    # 时间复杂度 : O((n + m)\log(n + m))O((n+m)log(n+m))。
    # 空间复杂度 : O(1)O(1)。
    def merge_1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)

    # 双指针
    # 时间复杂度 O(m+n)
    # 空间复杂度 O(m)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = nums1[:m]
        nums1[:]=[]# 清空列表
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if tmp[p1] < nums2[p2]: 
                nums1.append(tmp[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[p1 + p2:] = tmp[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]


# @lc code=end

if __name__ == '__main__':
    l1 = [1,2,3,0,0,0]
    l2 = [2, 5, 6]
    Solution().merge(l1,3,l2,3)
    print(l1)