#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, n in enumerate(nums):
            if target - n in nums[idx+1:]:
                return [idx, len(nums) - 1 - nums[::-1].index(target - n)]
# @lc code=end

