from typing import List
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            pile = max(gifts)
            gifts[gifts.index(pile)] = math.floor(math.sqrt(pile))
        return sum(gifts)

solution = Solution()
print(solution.pickGifts([25,64,9,4,100], 4))