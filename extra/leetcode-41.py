# First Missing Positive
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = set(nums)
        data = (i for i in range(1,len(arr)+2) if i not in arr)
        return min(data)

solution = Solution()
print(solution.firstMissingPositive([0,1,2,3]))
