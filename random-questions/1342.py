from time import time as perf_counter
import random

# Timing wrapper
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
    def numberOfSteps(self, num: int) -> int:
        i = 0
        while num != 0:
            num = num/2 if num%2==0 else num-1
            i+=1
        return i

solution = Solution()
print(solution.numberOfSteps(15654000121210212121211111005))
        