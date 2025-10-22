
"""
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Consider the number of unique elements in nums to be K. After removing duplicates,
return the number of unique elements k.
The first k elements of nums should contain the unique numbers in sorted order.
The remaining elements beyond index k - 1 can be ignored.

"""
class Solution:
    def remove_duplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Initialize slow pointer
        slow = 0

        # Iterate with fast pointer
        for fast in range(1, len(nums)):
            # check If a new unique element is found
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        # Return the new length (number of unique elements)
        return slow + 1


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = sol.remove_duplicates(nums)
    print("New length:", k)
    print("Array after removal:", nums[:k])
