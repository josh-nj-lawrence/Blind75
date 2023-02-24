# 1672 Richest Customer Wealth
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
    def maximumWealth(self, accounts):
        """
            Accounts: List[List[ints]]
            
            maxWealth: int (max wealth) 
        """
        return max([sum(cust) for cust in accounts])

solution = Solution()
accounts = [[random.randint(0,1000000) for _ in range(100)] for _ in range(random.randint(1000,10000))]
print(solution.maximumWealth(accounts))

