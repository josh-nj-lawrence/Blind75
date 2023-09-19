class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = bin(int(a,2) + (int(b,2)))
        return str(bin(int(ans,2)))[2:]
    
sol = Solution()
print(sol.addBinary('11','1'))

# Results: time 78.85% (32ms) space 97.22% (13.7MB)