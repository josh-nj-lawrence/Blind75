from typing import List
from collections import defaultdict
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        while nums:
            mx, mn = max(nums),min(nums)
            counts[(mx+mn)/2] = 1
            nums.remove(mx)
            nums.remove(mn)
        return len(counts)
    
sol = Solution()
print(sol.distinctAverages([1,100]))

# Results: 38.52% time (38ms) 95.51% space (13.8MB)