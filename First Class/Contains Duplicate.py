#Leetcode Number (217)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Sorting Approach
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if (nums[i-1] == nums[i]):
        #         return True
        # return False

        #Hash Map Approach
        # freq = {} # Initialize an empty hash map
        # for i in nums :
        #     if i in freq:
        #         return True
        #     freq[i] = 1
        # return False

        # Set Approach
        if (len(nums) != len(set(nums))):
            return True
        else: 
            return False

#Test the solution
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 1]  # Example with duplicates
    solution = Solution()
    result = solution.containsDuplicate(nums)
    print("Contains duplicate:", result)

    nums = [1, 2, 3, 4]  # Example without duplicates
    result = solution.containsDuplicate(nums)
    print("Contains duplicate:", result)
