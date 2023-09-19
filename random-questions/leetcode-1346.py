from typing import List

class Solution:
    def linear_search(self, nums, num):
        """
            Retruns true if num exists in nums
        """
        for x in nums:
            print(x, num)
            if x == num and nums.index(x) != nums.index(num):
                return True
        print("Inside fnc")
        return False


    def checkIfExist(self, arr: List[int]) -> bool:
        if arr is None:
            print("If None")
            return False
        for x in arr:
            if self.linear_search(arr, 2*x):
                return True
        print("Else") 
        return False

class Solution2:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for num in arr:
            if 2 * num in s: return True
            if not num % 2 and num // 2 in s: return True
            s.add(num)
        return False

solution = Solution2()
print(solution.checkIfExist([-2,0,10,-19,4,6,-8]))