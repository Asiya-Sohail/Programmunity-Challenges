#Leetcode Number (215)

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

# Test the solution
if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]  # Example input
    k = 2  # Find the 2nd largest element
    solution = Solution()
    result = solution.findKthLargest(nums, k)
    print("The", k, "th largest element is:", result)
