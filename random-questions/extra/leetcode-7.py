from typing import List
class Solution:
    def reverse(self, x: int) -> int:
        if x is None:
            return None
        elif x<0:
            return int("-" + str(abs(x))[::-1]) if int("-" + str(abs(x))[::-1]) > (-pow(2,31)) else 0
        return int(str(x)[::-1]) if int(str(x)[::-1]) < pow(2,31)-1 else 0
solution = Solution()
print(solution.reverse(-123))