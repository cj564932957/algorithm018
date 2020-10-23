'''
Description: 
Author: chen
Date: 2020-10-23 18:45:02
LastEditTime: 2020-10-23 21:52:33
LastEditors: chen
FilePath: /algorithm018/week01/homework/leetcode_189.py
'''
#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Medium (43.31%)
# Likes:    720
# Dislikes: 0
# Total Accepted:    173.1K
# Total Submissions: 399.6K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
#
# 示例 2:
#
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
# 说明:
#
#
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。
#
#
#

# @lc code=start


class Solution:

    def rotate_1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums[-1])
            nums.pop()
        return nums

    def rotate(self, nums: List[int], k: int) -> None:
        """
        三次旋转
        [1,2,3,4,5,6,7]
        1.旋转 前半部分   （0,n-k-1） ->[4,3,2,1,5,6,7] 
        2.旋转后边的       (n-k,n-1) ->[4,3,2,1,7,6,5] 
        3.旋转全部         (0,n-1)   ->[5,6,7,1,2,3,4,] 
        """
        def swap(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1; r -= 1
        
        n = len(nums)
        k %= n
        swap(0, n-k-1)
        swap(n-k, n-1)
        swap(0, n-1)




# @lc code=end
