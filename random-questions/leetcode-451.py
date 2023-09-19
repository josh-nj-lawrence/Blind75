class Solution:
    def frequencySort(self, s: str) -> str:
        letters = {}
        for c in s:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        print(letters)
        ans = ""
        letters_sorted = reversed(sorted(letters.keys(), key = lambda ele: letters[ele]))
        for l in letters_sorted:
            ans += l*letters.get(l)
        return ans
    
sol = Solution()
print(sol.frequencySort("asdfjlkjnxcknasjdsflkajlkj"))
