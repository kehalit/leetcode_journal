"""
The "famous" Two sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in index_map:
                return [index_map[diff], i]
            else:
                index_map[num] = i

        raise ValueError("No two numbers add up to the target.")





if __name__ == "__main__":
    result = Solution()
    print(result.twoSum([2, 7, 11, 15], 9))