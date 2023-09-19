from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, x in enumerate(nums):
            if x == target:
                return i
            if target < x:
                return i
        return len(nums)

solution = Solution()
print(solution.searchInsert([1,2,5,7,9], 10))