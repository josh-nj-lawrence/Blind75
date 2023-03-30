from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in reversed(range(len(digits))):
            if digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    return [1] + digits
                digits[i-1] += 1
        return digits
    
    # Results: time 70.4% (33ms) space 94.7% (13.8MB)