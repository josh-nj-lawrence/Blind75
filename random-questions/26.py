#Q26 Remove duplcates from sorted array
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num = 0
        for i, x in enumerate(nums):
            if i < len(nums)-1:
                if nums[i+1] == x:
                    # Shift over duplicate
                    for j in range(len(nums)-i-2):
                        nums[i+j] = nums[i+j+1]

class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        init_len = len(nums)
        for i, x in enumerate(nums):
            keep_popping = True
            while keep_popping and i < len(nums)-1:
                if nums[i+1] == x:
                    nums.pop(i)
                else:
                    keep_popping = False
        ret_val = len(nums)
        for x in range(len(nums)+1,init_len+1):
            nums.append(0)
        return ret_val
nums = [1,1]
print(nums)
solution = Solution2()
print(solution.removeDuplicates(nums))
print(nums)