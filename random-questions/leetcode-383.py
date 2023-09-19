# Q383
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
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = list(magazine)
        for c in ransomNote:
            if c in letters:
                letters.remove(c)
            else:
                return False
        return True

solution = Solution()
print(solution.canConstruct("aa", "aab"))