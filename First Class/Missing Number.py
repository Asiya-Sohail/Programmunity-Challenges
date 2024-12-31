#Leetcode Number (268)

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] != i:
                return i
        return n

# Test the solution
if __name__ == "__main__":
    nums = [3, 0, 1]  # Example input
    solution = Solution()
    result = solution.missingNumber(nums)
    print("The missing number is:", result)

    nums = [0, 1, 2, 4, 5]  # Another test case
    result = solution.missingNumber(nums)
    print("The missing number is:", result)

