from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            row = [None for _ in range(i)]
            row[0], row[-1] = 1,1

            for j in range(1, len(row)-1):
                row[j] = ans[i-1][j-1] + ans[i-1][j]

            ans.append(row)
        return ans

# Results: time 73.78% (33ms) space 54.89% (13.8MB)