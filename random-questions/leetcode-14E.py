from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs, key=len)
        for word in strs:
            while len(smallest) > 0:
                if word.startswith(smallest):
                    break
                else:
                    smallest = smallest[:-1]

        return smallest
    
sol = Solution()
print(sol.longestCommonPrefix(["a","ab"]))

# Results: 56.41% time (37ms) 79.45% space (13.8MB)