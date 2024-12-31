#Leetcode Number (136)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Bitwise XOR Approach
        xor = 0
        for i in range(len(nums)):
            xor = xor ^ nums[i]
        return xor

# Test the solution
if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    solution = Solution()
    result = solution.singleNumber(nums)
    print("Single number:", result)
