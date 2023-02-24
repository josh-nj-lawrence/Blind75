from collections import Counter
from typing import List
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        b1_count = Counter(basket1)     
        for fruit in basket2: b1_count[fruit] -= 1
        to_switch = []
        for k, v in b1_count.items():
            if v % 2 == 1:
                return -1
            to_switch += [k] * abs(v//2)
        
        minx = min(basket1+basket2)
        to_switch.sort()
        return sum(min(2*minx, x) for x in to_switch[0:len(to_switch)//2])




solution = Solution()
print(solution.minCost([4,2,2,2], [1,4,1,2]))
