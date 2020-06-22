#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:

    def twoSum_bf(self, numbers: List[int], target: int) -> List[int]:
        #brute-force, TC = O(N^2)
        size = len(numbers)
        for i in range(size-1):
            for j in range(size):
                sum = numbers[i] + numbers[j]
                if sum == target:
                    return [i, j]

        return []


#main

l = [10, 23, 1, 5, 100]
l.sort()
print (l)
value = Solution().twoSum_bf(l, 11)
print(value)
