'''
Description: 
Author: chen
Date: 2020-10-23 22:53:51
LastEditTime: 2020-10-23 23:16:49
LastEditors: chen
FilePath: /algorithm018/week01/homework/leetcode_283.py
'''
#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (62.54%)
# Likes:    780
# Dislikes: 0
# Total Accepted:    225.5K
# Total Submissions: 360.3K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
# 说明:
#
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
#
#
#

# @lc code=start


class Solution:
    """
    思路1:
        1.遍历列表，记录所有0的个数K，并删除0
        2.list.append(0)*K 
        时间复杂度O(n+k) 空间复杂度O(1)
    思路2:双指针
        1.若为空，直接结束
        2.慢指针i ，快指针j
        3.若j的值不为0，则 i ,j 互换 同时 i++
        4.若j的值为0，则j++  ，快指针左边必是非0
        
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
	    # 第一次遍历的时候，j指针记录非0的个数，只要是非0的统统都赋给nums[j]
        i = 0
        for j in range(len(nums)):
			# 当前元素!=0，就把其交换到左边，等于0的交换到右边
            if nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1


# @lc code=end
