# Remove Element
from typing import List 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        print(nums)
        for i, ele in enumerate(nums):
            # Check that ith position is val
            if ele == val:
                # Check how many instances there are
                vals = 1
                for x in range(i,len(nums)-2):
                    if nums[x+1] == val:
                        vals +=1
                print(f"Number of vals: {vals}")
                # Shift remaining nums over vals
                for j in range(i,len(nums)-vals):
                    print(j)
                    nums[j] = nums[j+vals]
                del nums[len(nums)-vals:]
                return len(nums) - vals

# Built in solution
class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

nums = [0,1,2,2,3,0,4,2] # [0,0,1,2,2,2,3,4]

solution = Solution()
print(solution.removeElement(nums, 2))
print(nums)

nums1 = [0,1,2,2,3,0,4,2]
val = 2
expectedNums = [0,1,4,0,3]
k = solution.removeElement(nums1, val)

assert k == len(expectedNums)
for i in range(5):
    assert nums[i] == expectedNums[i]
