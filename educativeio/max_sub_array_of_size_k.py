'''
https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP

Given an array of positive numbers and a positive number ‘k’,
find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''


def max_sub_array_of_size_k_bf(k, arr):
	window_sum = 0
	max_num = 0
	
	for i in range(len(arr)-k+1):
		window_sum = 0
		for j in range(i, i+k):
			window_sum += arr[j]
		max_num = max(window_sum, max_num)
	return max_num


def max_sub_array_of_size_k(k, arr):
	max_sum, window_sum = 0, 0
	window_start = 0
	
	
	
	return max_sum


# [2, 1, 5, 1, 3, 2], k=3 -> 9
print(max_sub_array_of_size_k_bf(3, [2, 1, 5, 1, 3, 2]))

# [2, 3, 4, 1, 5], k=2 -> 7
print(max_sub_array_of_size_k_bf(2, [2, 3, 4, 1, 5]))
