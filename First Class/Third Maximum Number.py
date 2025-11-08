# Leetcode 414

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))           
        nums.sort(reverse=True)          
        if len(nums) >= 3:
            return nums[2]               
        else:
            return nums[0]               

if __name__ == "__main__":
    nums = [2, 2, 3, 1]

    obj = Solution()
    result = obj.thirdMax(nums)

    print("Input:", nums)
    print("Third Maximum Number:", result)
