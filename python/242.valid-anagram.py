#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for letter in s:
            t = t.replace(letter, '', 1)

        return len(t) == 0
# @lc code=end

