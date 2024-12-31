#Leetcode Number (167)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            sm = nums[l] + nums[r]
            if sm == target:
                return [l + 1, r + 1]
            elif sm < target:
                l += 1
            else:
                r -= 1

# Test the solution
if __name__ == "__main__":
    nums = [2, 7, 11, 15]  # Example input (assumes the array is sorted)
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print("Indices of numbers that sum to target:", result)
