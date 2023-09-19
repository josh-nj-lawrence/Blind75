# Q409 Longest Palindrome
# Start at 10:49 pm - 11:06 pm
class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {} # map of unique letters and their counts

        # Count letters
        for chr in s:
            if chr in letters:
                # Increment
                letters[chr] += 1
            else:
                # Add
                letters[chr] = 1
        # Build palendrome
        # Can only have 1 letter with odd count, choose one with most instances
        remove = 0
        for c in letters.values():
            remove += c % 2

        print(letters)
        return len(s) - remove + 1 if remove > 0 else len(s) - remove

sol = Solution()
print(sol.longestPalindrome('civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'))