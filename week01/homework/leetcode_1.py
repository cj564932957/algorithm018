'''
Description: 
Author: chen
Date: 2020-10-23 22:48:54
LastEditTime: 2020-10-23 22:53:10
LastEditors: chen
FilePath: /algorithm018/week01/homework/leetcode_1.py
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (49.71%)
# Likes:    9401
# Dislikes: 0
# Total Accepted:    1.5M
# Total Submissions: 3M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
# 
# 
# 
# 示例:
# 
# 给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 
# 
#

# @lc code=start
class Solution:
    """
    通过哈希表（字典）
    1.num2=target-num1
    2.遍历列表，判断nums2 是否在字典中，若不在则将列表的数据散列到字典中： {value:index}，
        若存在，则返回 dicts[value]
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}
        for i, num in enumerate(nums):
            if target - num in dicts:
                return [dicts[target - num], i]
            dicts[nums[i]] = i
        return []
# @lc code=end

