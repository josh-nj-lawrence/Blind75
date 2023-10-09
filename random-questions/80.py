from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
        Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.
        
        Args:
        - nums: A list of integers representing the sorted array.
        
        Returns:
        - An integer representing the new length of the array after removing duplicates.
        """
        if not nums:
            return 0
        
        i = 0
        count = 1
        
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                count += 1
                if count <= 2:
                    i += 1
                    nums[i] = nums[j]
            else:
                i += 1
                nums[i] = nums[j]
                count = 1
        
        return i + 1
