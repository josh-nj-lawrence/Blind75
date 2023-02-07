from collections import defaultdict
from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ["a","e","i","o","u"]
        words_checked = [1 if word[0] in vowels and word[-1] in vowels else 0 for word in words]
        prefix = [0] * (len(words)+1)
        ans = []
        for n in range(len(words)):
            prefix[n+1] = prefix[n]+ (1 if words[n][0] in vowels and words[n][-1] in vowels else 0)
        for l,r in queries:
            ans.append(prefix[r+1] - prefix[l])
        return ans

solution = Solution()
print(solution.vowelStrings(["aba","bcb","ece","aa","e"],[[0,2],[1,4],[1,1]]))