#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {char: s.count(char) for char in set(s)}
        t_dict = {char: t.count(char) for char in set(t)}
        return s_dict == t_dict
# @lc code=end

