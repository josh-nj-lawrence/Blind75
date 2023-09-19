from typing import List

# Readable solution
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = [x for x in nums if x%2 == 1]
        even = [x for x in nums if x not in odd]
        return even + odd

# Fast and InPlace Solution
class Solution2:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if None in nums:
            return nums
        p1, p2 = 0, len(nums)-1
        while p1<p2:
            if nums[p1]%2 == 1:
                if nums[p2]%2 == 0:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                else:
                    p2-=1
            else:
                p1+=1
        return nums


solution = Solution2()
print(solution.sortArrayByParity([0]))