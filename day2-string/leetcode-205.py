# Isomorfic String
"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character, but a character may map to itself.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        # Loop over s, map s char to t char, check if invalid and break
        for i, c in enumerate(s):
            if map.get(c) == None and t[i] not in map.values():
                map.update({c:t[i]})
            elif map.get(c) == t[i]:
                pass
            else:
                return False
            print(map.get(c))
            print(map)
            print(i)
            print(c not in map.values())
        # if you've gotten to this point then they're isomorphic
        return True

solution = Solution()
print(solution.isIsomorphic("badc","baba"))