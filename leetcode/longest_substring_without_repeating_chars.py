class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        l = len(s)
        ans = 0
        for i in range(0, l):
            print(s[:i+1])

        return ans

    def is_unique(self, s) -> bool:
        char_seen = []
        for c in s:
            if c in char_seen:
                return False
            char_seen.append(c)
        return True


#print(Solution().lengthOfLongestSubstring('abcabcbb'))  # expect 3(abc)
#print(Solution().lengthOfLongestSubstring('bbbbb'))  # expect 1(b)
#print(Solution().lengthOfLongestSubstring('pwwkew'))  # expect 2
#print(Solution().lengthOfLongestSubstring(''))  # expect 0

print(Solution().lengthOfLongestSubstring('abcde'))

