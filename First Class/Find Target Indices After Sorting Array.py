#Leetcode Number (2089)

class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Brute Force Approach
        # nums.sort() # n log n complexity
        # result = []
        # for i in range(0, len(nums)):
        #     if (target == nums[i]):
        #         result.append(i)
        # return result

        # Two Count Approach # n complexity
        target_count = 0
        target_less = 0
        for i in range(0, len(nums)):
            if nums[i] < target:
                target_less += 1
            if nums[i] == target:
                target_count += 1
        
        # return [i for i in range(target_less, target_less + target_count)]
        return list(range(target_less, target_less + target_count))
        
        #Can also be solved by using lowerbound and upperbound , but first need to sort (O(log(n)))

        #Can also be solved using binary search, finding and pushing lower indexes of that target then pushing index of target then finding and pushing upper indexes of that target


        # Test the solution
if __name__ == "__main__":
    nums = [1, 2, 5, 2, 3]
    target = 2
    solution = Solution()
    result = solution.targetIndices(nums, target)
    print("Target indices:", result)