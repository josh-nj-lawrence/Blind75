# 412 Fizz Buzz
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
    def fizzBuzz(self, n):
        """
            n: int
            
            answer: List[str]
        """
        answer = [x for x in range(1,n+1)]
        for i, ele in enumerate(answer):
            answer[i] = "FizzBuzz" if ele % 3 == 0 and ele % 5 == 0 else "Fizz" if ele % 3 == 0 else "Buzz" if ele % 5 == 0 else str(ele)
        return answer

solution = Solution()
print(solution.fizzBuzz(15)) 

