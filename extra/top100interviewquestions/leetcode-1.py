# Two Sums

class Solution:
    def twoSum(self, nums, target):
        p1, p2 = 0, len(nums)-1
        # Sort nums in order
        nums = sorted(nums)
        # Calc 
        while p1 < p2:
            if (nums[p1] + nums[p2]) == target:
                return [p1,p2]
            elif (nums[p1] + nums[p2]) < target:
                p1+=1
            else:
                p2-=1
        return "No Solutions"
solution = Solution()
print(solution.twoSum(nums=[3,2,4], target=6))