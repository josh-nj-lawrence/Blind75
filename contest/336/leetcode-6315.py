from typing import List
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0
        for word in words[left:right+1]:
            if self.isVowelString(word):
                ans += 1
        return ans
        
    def isVowelString(self, word: str) -> bool:
        vowels = ['a','e','i','o','u']
        return word and word[0] in vowels and word[-1] in vowels

sol = Solution()
print(sol.vowelStrings(["hey","aeo","mu","ooo","artro"], 1, 4))
