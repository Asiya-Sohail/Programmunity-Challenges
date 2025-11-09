# Leetcode 15

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        nums.sort()
        res = set()
        for i in range(length):
            left = i + 1
            right = length - 1
            while left < right:
                summation = nums[i] + nums[left] + nums[right]
                if summation < 0:
                    left += 1
                elif summation > 0:
                    right -= 1
                else:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        return [list(triplet) for triplet in res]


# -------- Input and Output Example --------
if __name__ == "__main__":
    # Example Input
    nums = [-1, 0, 1, 2, -1, -4]

    # Create object
    obj = Solution()
    
    # Call the method
    result = obj.threeSum(nums)
    
    # Output
    print("Input:", nums)
    print("Triplets that sum to 0:", result)
