'''
Description: 
Author: chen
Date: 2020-11-01 19:28:32
LastEditTime: 2020-11-01 19:40:33
LastEditors: chen
FilePath: /algorithm018/week02/homework/剑指 Offer 49. 丑数.py
'''
#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (54.36%)
# Likes:    417
# Dislikes: 0
# Total Accepted:    37.9K
# Total Submissions: 69.6K
# Testcase Example:  '10'
#
# 编写一个程序，找出第 n 个丑数。
# 
# 丑数就是质因数只包含 2, 3, 5 的正整数。
# 
# 示例:
# 
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 
# 说明:  
# 
# 
# 1 是丑数。
# n 不超过1690。
# 
# 
#

# @lc code=start
class Solution:
    """
    丑数 == 某较小丑数 \times× 某因子
    
    设动态规划列表 dp ，dp[i] 代表第 i+1 个丑数。
    转移方程：
        当索引 a, b, c 满足以下条件时， dp[i] 为三种情况的最小值；
        每轮计算 dp[i]后，需要更新索引 a, b, c的值，使其始终满足方程条件。
            实现方法：分别独立判断 dp[i]和 dp[a]*2, dp[b]×3 , dp[c]×5 的大小关系，
            若相等则将对应索引 a , b , c 加 1 

    初始状态： dp[0] = 1dp[0]=1 ，即第一个丑数为 11 ；
    返回值： dp[n-1] ，即返回第 n 个丑数。
    """
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]


# @lc code=end

