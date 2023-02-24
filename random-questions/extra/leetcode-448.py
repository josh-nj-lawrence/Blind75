from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        expected = [x for x in range(1,len(nums)+1)]
        return list(set(expected)-set(nums))

solution = Solution()
print(solution.findDisappearedNumbers([1,1]))