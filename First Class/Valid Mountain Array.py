#Leetcode Number (941)

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False

        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1

# Test the solution
if __name__ == "__main__":
    arr = [0, 3, 2, 1]  # Example input
    solution = Solution()
    result = solution.validMountainArray(arr)
    print("Is the array a valid mountain array?", result)

    arr = [3, 5, 5]  # Another test case
    result = solution.validMountainArray(arr)
    print("Is the array a valid mountain array?", result)
