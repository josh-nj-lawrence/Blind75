#Duplicate Zeros
from tools import timing
from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        x = 0
        while x < len(arr)-1:
            if arr[x] == 0:
                # duplicate, shift remaining elms and jump dupped index
                # Make room
                for i in reversed(range(x+1, len(arr)-1)):
                    arr[i+1] = arr[i]
                # Insert Duplicate
                arr[x+1] = 0
                #arr.insert() method would eliminate this implementation
                x+=2
            else:
                x+=1

a1 = [1,0,3,0,5,6,0,8,9,10,0,0,1,0,1]
print(a1)
solution = Solution()
solution.duplicateZeros(a1)
print(a1)