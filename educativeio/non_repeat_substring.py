"""
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".

"""
def non_repeat_substring(str1):
    window_start = 0
    max_length = 0
    char_index_map = {}
    right_char = ''

    for window_end in range(len(str1)):
        right_char = str1[window_end]

        # if right_char exists in char_index_map, that means there is a duplicate
        #   - move window_start at the index of right_char +1
        if right_char in char_index_map:
            window_start = char_index_map[right_char] + 1

        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def non_repeat_substring_bf(str1):
    max_length = 0
    lst = [str1[i:j] for i in range(len(str1)) for j in range(i + 1, len(str1) + 1)]
    for s in lst:
        if contains_unique_chars(s):
            max_length = max(len(s), max_length)

    return max_length


'''
Python program to check if a string contains all unique characters
'''


def contains_unique_chars(str1):
    # https://www.geeksforgeeks.org/python-get-all-substrings-of-given-string/
    char_set = [False] * 128

    for ch in str1:
        if char_set[ord(ch)]:
            return False
        else:
            char_set[ord(ch)] = True
    return True


def main():
    #print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("bbbc")))
    #print("Length of the longest substring: " + str(non_repeat_substring("abccde")))

    #print("Does string abca has unique chars?: " + str(contains_unique_chars('abca')))
    #print("Does string abc has unique chars?: " + str(contains_unique_chars('abc')))
    #print("Does string '' has unique chars?: " + str(contains_unique_chars('')))

    #print("Length of the longest substring(brute force): " + str(non_repeat_substring_bf("abc")))
    #print("Length of the longest substring(brute force): " + str(non_repeat_substring_bf("abbbb")))
    #print("Length of the longest substring(brute force): " + str(non_repeat_substring_bf("abccde")))


main()
