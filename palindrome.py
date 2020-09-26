class Solution:
    def isPalindrome_rik(self, x: int) -> bool:
        string_x = str(x)
        if string_x[::-1] == string_x:
            print('True')
            return True
        print('False')
        return False


    def isPalindrome(self, x: int) -> bool:
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x = x/10
        print(f'{x} {reverted_number}')
        return (x == reverted_number) or (x == reverted_number / 10)


s = Solution()
print(s.isPalindrome(123))
print(s.isPalindrome(1))
print(s.isPalindrome(121))
print(s.isPalindrome(44))
