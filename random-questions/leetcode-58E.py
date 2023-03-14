class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(" ")
        s = s.split(" ")
        return len(s[-1])
    
sol = Solution()
print(sol.lengthOfLastWord("hellow world"))

# Results: 67.90% time (31ms) 28.99% space(14MB)