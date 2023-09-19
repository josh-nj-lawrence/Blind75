from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j = 0
        smallest = min(len(x) for x in strs)
        if not strs:
            return ""
        for i in range(1,smallest):
            y = strs[0][0:i]
            for j in range(1, len(strs)):
                if strs[j][:i] == y:
                    pass
                else:
                    return strs[0][:i]
        return ""

solution = Solution()
print(solution.longestCommonPrefix(["a"]))