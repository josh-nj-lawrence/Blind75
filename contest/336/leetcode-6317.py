from typing import List 
from collections import OrderedDict
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        hashmap = OrderedDict()
        ans, x = 0, 0
        hashmap[0] = 1
        for i in range(len(nums)):
            x = x | nums[i]
            try:
                if hashmap[x] != hashmap.values()[-1]:
                    ans = ans + hashmap[x]
            except KeyError:
                pass
            try:
                hashmap[x] += 1
            except KeyError:
                pass
        return ans

sol = Solution()
print(sol.beautifulSubarrays([4,3,1,2,4]))