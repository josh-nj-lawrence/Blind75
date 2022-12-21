# Merge Sorted Arrays
from typing import List

# Sol1 not implemented correctly
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0,0 # Array Indecies
        while i < m and j < n:
            if nums2[j] < nums1[i]:
                # Insert at start
                nums1.insert(i,nums2[j])
                i += 1 # Increment i to account for shift in values of interest
                j += 1
            elif nums2[j] < nums1[i+1]: # This will have index overflow issues
                # If Greater than first value but less than next value insert
                nums1.insert(i+1, nums2[j])
                i += 1
                j += 1
            else:
                # nums1[i] and nums1[i+1] < nums2 
                i += 1

# Easy solution
class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1 = sorted(nums1)

sol1 = Solution()
num1, num2, m, n = [1,3,5,0,0,0], [2,3,4], 3, 3
sol1.merge(num1, m, num2, n)
print(num1)
