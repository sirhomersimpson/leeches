'''
https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP

Given an array of positive numbers and a positive number ‘k’,
find the maximum sum of any contiguous subarray of size ‘k’.
'''


def max_sub_array_of_size_k(k, arr):

    window_sum = 0
    max_num = 0
    # 2 3 4 1 5 ; k =2

    for i in range(len(arr)-k + 1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += arr[j]

        max_num = max(window_sum, max_num)
    return max_num


def max_sub_array_of_size_k_sliding_window(k, arr):

    max_sum = 0
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum

'''
2,3,4,1,5
    |
window_start = 1
window_end = 1 
window_sum = 7
max_sum = 5
k=2
'''