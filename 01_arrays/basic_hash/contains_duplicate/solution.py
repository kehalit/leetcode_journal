"""
Write a function find_duplicates(nums) that takes a list of integers and returns a list of all the duplicate
 numbers (each duplicate should appear only once in the result).

 inpute = [3,5,6,7,3,5]
 result = [3, 5]
 Explanation of Thought Process

"""

class Solution(object):
    def find_duplicates(self, nums):
        """
            :type nums: List[int]
            rtype: bool
        """
        seen = set()
        duplicates = set()
        for num in nums:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)

        return list(duplicates)


if __name__ == "__main__":
    result = Solution()
    print(result.find_duplicates([2,2,6,6,7,8,9,1,1]))



