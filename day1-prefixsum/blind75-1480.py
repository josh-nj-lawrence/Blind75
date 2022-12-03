# Running Sum of 1d Array

class Solution:
    def runningSum(self, nums):
        total = 0
        running_sum = []
        for i in nums:
            total += i
            running_sum.append(total)
        return running_sum

solution = Solution()
print(solution.runningSum([1,2,3,4,5]))