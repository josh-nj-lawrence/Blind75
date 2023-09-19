# Find Pivot Index
class Solution:
    def pivotIndex(self, nums) -> int:
        for i, num in enumerate(nums):
            if (sum(nums[0:i]) == sum(nums[i+1:(len(nums))])):
                return i
                #print(str(i) + " " + str(sum(nums[0:i])) + " " + str(sum(nums[i+1:(len(nums))])))
        return -1

solution = Solution()
print(solution.pivotIndex([2,1,-1]))

""" Results
Runtime: 8266 ms, faster than 5.23% of Python3 online submissions for Find Pivot Index.
Memory Usage: 15.3 MB, less than 49.20% of Python3 online submissions for Find Pivot Index.
"""