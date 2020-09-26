class Solution:

    def reverse(self, num) -> int:
        r = 0
        while num > 0:
            r = r*10 + num%10
            num = num//10
        return r


print(Solution().reverse(1234))
