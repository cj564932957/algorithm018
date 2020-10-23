'''
Description: 
Author: chen
Date: 2020-10-23 18:44:11
LastEditTime: 2020-10-23 19:15:27
LastEditors: chen
FilePath: /algorithm018/week01/homework/leetcode_26.py
'''
#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (51.98%)
# Likes:    1688
# Dislikes: 0
# Total Accepted:    450.1K
# Total Submissions: 865.5K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
#
#
#
# 示例 1:
#
# 给定数组 nums = [1,1,2],
#
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
#
# 你不需要考虑数组中超出新长度后面的元素。
#
# 示例 2:
#
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
#
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
#
# 你不需要考虑数组中超出新长度后面的元素。
#
#
#
#
# 说明:
#
# 为什么返回数值是整数，但输出的答案是数组呢?
#
# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
#
# 你可以想象内部操作如下:
#
# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);
#
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
#
#
#
from typing import List
# @lc code=start


class Solution:
    """
    思路1:
        1.排序后的数组，则重复元素是相邻的
        2.使用stack，数据和栈顶元素比较，不存在，则入栈,空间复杂度O(n),不满足条件
    思路2:
        采用双指针的方式，遍历数组，
        1.慢指针i，快指针j
        2.当 i和 j的元素相同时，推动j向下走，i不动
        3.当i和j不同时，则此时 交换 i+1 和j的数据
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        i = 0 # 因为nums 有序，故可以直接一次for循环即可
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        return i+1


# @lc code=end