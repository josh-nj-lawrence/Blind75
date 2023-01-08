from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,x in enumerate(nums):
            for j,y in enumerate(nums):
                if i != j and x+y == target:
                    return [i,j]

"""
    More efficient solution would be loop over all elements and create dict of compliments.
    Then return the pair where num and it's compliment are in the input array
"""
                    
solution = Solution()
print(solution.twoSum([3,3],6))