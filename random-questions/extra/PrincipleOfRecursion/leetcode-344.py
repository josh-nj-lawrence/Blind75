#Q344
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

solution = Solution()
a = ['h','e','l','l','o']
solution.reverseString(a)
print(a)