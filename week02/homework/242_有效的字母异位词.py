#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode-cn.com/problems/valid-anagram/description/
#
# algorithms
# Easy (61.74%)
# Likes:    268
# Dislikes: 0
# Total Accepted:    149.7K
# Total Submissions: 242.1K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
#
# 说明:
# 你可以假设字符串只包含小写字母。
#
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#
#

# @lc code=start
class Solution:
    """
            return collections.Counter(s) == collections.Counter(t)
    """

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in t:
            if j in d :
                d[j] -= 1
            else:
                return False
        for i in d.values():
            if i != 0:
                return False
        return True

# @lc code=end
