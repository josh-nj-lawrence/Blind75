from tools import timing
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x**2 for x in nums])

solution = Solution()
print(solution.sortedSquares([-9,3,5,7,9,11,15,24,37]))