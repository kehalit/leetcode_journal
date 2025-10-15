class Solution(object):
   def find_missing_number(self,nums):
        """
            :type nums: List[int]
            :rtype: int
        """
        if not nums:
            return []

        nums.sort()
        missing = []

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                missing.extend(range(nums[i] + 1, nums[i + 1]))

        return missing


if __name__ == "__main__":
    result = Solution()
    print(result.find_missing_number([8,9,10,20,21,22]))