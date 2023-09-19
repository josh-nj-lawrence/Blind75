from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        stack = [(0,'')]
        combinations = []
        while stack:
            index, currentString = stack.pop()
            if index == len(digits):
                combinations.append(currentString)
            else:
                for letter in map[digits[index]]:
                    stack.append((index+1, currentString + letter))

        return combinations

solution = Solution()
print(solution.letterCombinations("23"))
