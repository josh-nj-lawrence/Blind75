from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        out_of_order = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                out_of_order +=1 
        return out_of_order

solution = Solution()
print(solution.heightChecker([1,3,4,2,5,6,4]))