"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        max_length = 0
        char_index_map = {}
        # Step 1. Go through the windown
        for window_end in range(len(s)):
            right_char = s[window_end]
            
            # Step 2. If we see the right_char, we need to re-adjust the window
            if right_char in char_index_map:
                window_start = char_index_map[right_char]+1
            
            # Step 3. Store the window end
            char_index_map[right_char] = window_end
            # Step 4. Calculate the maximum
            max_length = max(max_length, window_end-window_start+1)
            
        return max_length
     
    
print(Solution().lengthOfLongestSubstring('aabcde')) # expects
print(Solution().lengthOfLongestSubstring('abba'))

