'''
Description: 
Author: chen
Date: 2020-10-29 19:13:15
LastEditTime: 2020-11-01 19:13:49
LastEditors: chen
FilePath: /algorithm018/week02/homework/15.三数之和.py
'''
#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (29.83%)
# Likes:    2709
# Dislikes: 0
# Total Accepted:    354K
# Total Submissions: 1.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if(not nums or n < 3):
            return []
        nums.sort()  # O(nlogn)
        for i in range(n):
            if(nums[i] > 0):
                return res
            if(i > 0 and nums[i] == nums[i-1]):  # i>0 防止 i-1 为负 取最后的值
                # 去除重复解
                continue
            L = i+1
            R = n-1
            while(L < R):
                if(nums[i]+nums[L]+nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while(L < R and nums[L] == nums[L+1]):
                        L = L+1
                    while(L < R and nums[R] == nums[R-1]):
                        R = R-1
                    L = L+1
                    R = R-1
                elif(nums[i]+nums[L]+nums[R] > 0):
                    R = R-1
                else:
                    L = L+1
        return res


# @lc code=end
