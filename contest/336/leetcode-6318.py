from typing import List
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        """
            Basically what we need to determine is overlay all of the task start:end windows and see how you can line up the duration windows
            such that we minimize the computers run time.
        """        
