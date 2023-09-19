from tools import timing
from typing import List

class Solution:
    @timing.method_timer
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max, count = 0, 0
        for i in nums:
            count = (count+1 if i==1 else 0)
            max = (count if count>=max else max)
        return max

solution = Solution()
print(solution.findMaxConsecutiveOnes([1,1,1,1,1,0,1,1,1,0,1]))