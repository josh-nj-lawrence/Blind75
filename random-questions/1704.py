# Determine if String Halves are Alike
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
    def halvesAreAlike(self, s):
        i = len(s)//2
        a, b = s[:i], s[i:]
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        print(a, b)
        return True if len([x for x in a if x in vowels]) == len([x for x in b if x in vowels]) else False       

solution = Solution()
print(solution.halvesAreAlike("asdffdsaaa"))