from tools import timing
from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1 if len(str(x))%2 == 0 else 0 for x in nums])

solution = Solution()
print(solution.findNumbers([123,2232,3222,41,523,6,7,8,9]))