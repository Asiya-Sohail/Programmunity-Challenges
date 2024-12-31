#Leetcode Number (169)

from typing import List

class Solution(object):
    def majorityElement(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        major = None
        mx = -float('inf')
        for i in nums:
            if freq[i] > mx:
                mx = freq[i]
                major = i

        return major

# Test the solution
if __name__ == "__main__":
    nums = [3, 2, 3]  # Example input
    solution = Solution()
    result = solution.majorityElement(nums)
    print("The majority element is:", result)

    nums = [2, 2, 1, 1, 1, 2, 2]  # Another test case
    result = solution.majorityElement(nums)
    print("The majority element is:", result)
