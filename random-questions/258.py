class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

sol = Solution()
print(sol.addDigits(38))
            
# Results: 58.73% time (35ms) 41.67% space (13.8MB)