from typing import List
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # Sort nums in reverse order
        nums.sort(reverse=True)
        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
            
        ans = 0
        for x in prefix:
            if x > 0:
                ans += 1
        return ans
    
sol = Solution()
print(sol.maxScore([2,-1,0,1,-3,3,-3]))