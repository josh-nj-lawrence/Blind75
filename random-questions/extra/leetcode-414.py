from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        for i in range(len(nums)-1):
            # If dup remove
            if nums[i+1] == nums[i]:
                nums.remove(nums[i+1])
        print(nums)
class Solution2:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) >= 3:
            checked = set()
            count = 0
            nums.sort()
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] not in checked:
                    if count == 2:
                        return nums[i]
                    else:
                        checked.add(nums[i])
                        count += 1
            return max(nums)
        else:
            return max(nums)


solution = Solution2()
solution.thirdMax([2,2,3,1])