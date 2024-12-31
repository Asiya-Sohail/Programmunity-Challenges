#Leetcode Number (26)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1  # Write index
        for right in range(1, len(nums)):  # Read index
            if nums[right] != nums[left - 1]:
                nums[left] = nums[right]
                left += 1
        return left

# Test the solution
if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 4]  # Example input
    solution = Solution()
    new_length = solution.removeDuplicates(nums)
    print("New length:", new_length)
    print("Modified array:", nums[:new_length])

