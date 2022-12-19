# Running Sum of 1d Array
# rewritting with timing method and preallocation of memory
from time import time as perf_counter

def profiler(method):
    def wrapper_method(*arg, **kw):
        t = perf_counter()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' +
              "{:2.5f}".format(perf_counter()-t) + ' sec')
        return ret
    return wrapper_method

class Solution:
    @profiler
    def runningSum(self, nums):
        total = 0
        running_sum = []
        for i in nums:
            total += i
            running_sum.append(total)
        return running_sum

class Solution2:
    @profiler
    def runningSum(self, nums):
        total = 0
        running_sum = [0]*len(nums)
        for i, num in enumerate(nums):
            total += num
            running_sum[i] = total
        return running_sum

solution = Solution()
solution2 = Solution2()
nums = [x for x in range(100000000)]
solution.runningSum(nums)
solution2.runningSum(nums)