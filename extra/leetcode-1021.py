#Q1021 Remove outermost parentheses
from typing import List

# Not complete
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        count = 0
        for i,x in enumerate(s):
            if x == "(" and count == 0:
                count += 1
            elif x == "(" and count >= 1:
                count += 1
                ans += x
            elif x == ")" and count >= 1:
                count -= 1
            elif x == ")" and count == 0:
                count -= 1
                ans += x       
        return ans


class Solution2:
    def removeOuterParentheses(self, S: str) -> str:
        result = []
        counter = 1
        i = 1
        while i < len(S):
            counter += 1 if S[i] == "(" else -1
            if counter != 0:
                result.append(S[i])
            else:
                counter = 1
                i += 1
            i += 1
        return "".join(result)

solution2 = Solution2()
print(solution2.removeOuterParentheses("()()"))

solution = Solution()
print(solution.removeOuterParentheses("(()())(())"))
print(solution.removeOuterParentheses("(()())(())(()(()))"))
print(solution.removeOuterParentheses("()()"))