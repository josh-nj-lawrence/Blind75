from typing import List

# Fast Solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = [x for x in nums if x != 0]
        for i in range(len(non_zero)):
            nums[i] = non_zero[i]
        for i in range(len(non_zero), len(nums)):
            nums[i] = 0

# Lean Solution - 2 pointer, shift 2nd pointer if pointing to non-zero
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        pnt = 0
        for i in range(len(nums)):
            if nums[i] !=0 and nums[pnt] == 0:
                nums[i], nums[pnt] = nums[pnt], nums[i]
            if nums[pnt] != 0:
                pnt +=1
        
arr = [0,0,2,3,0,0,0,4,5,0,1]
solution = Solution2()
solution.moveZeroes(arr)
print(arr)