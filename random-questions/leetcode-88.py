# Merge Sorted Arrays
from typing import List

# Sol1 not implemented correctly
def insert(arr: List[int], x: int, j: int) -> List[int]:
    """
        shift elements in an array for insertion of x into index j
    """
    # Shift
    for i in reversed(range(j+1, len(arr)-1)):
        arr[i+1] = arr[i]
    # Insert
    arr[j] = x
    return arr

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        
        while p1 < m and p2 < n:
            if nums1[p1 + p2] > nums2[p2]:
                nums1[p1 + p2 + 1:] = nums1[p1 + p2:m + n - 1]
                nums1[p1 + p2] = nums2[p2]
                p2 += 1
            else:
                p1 += 1
        if p1 == m:
            nums1[p1 + p2:] = nums2[p2:]

# Easy solution
class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1 = sorted(nums1)

sol1 = Solution()
num1, num2, m, n = [1,2,3,0,0,0], [2,5,6], 3, 3
sol1.merge(num1, m, num2, n)
print(num1)
