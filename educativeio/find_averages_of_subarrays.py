'''
https://www.educative.io/courses/grokking-the-coding-interview/7D5NNZWQ8Wr

k=1
1, 3, 2

1+3 i =0
3+2 i =1

N=7
1,5,2,3,4,2,10 k = 2
0 1 2 3 4 5 6
1,5 i =0
5,2
2,3
3,4
4,2
2,10 = 6
'''


def find_averages_of_sub_arrays_bf(k, arr):
    result = []
    for i in range(len(arr) - k + 1):
        _sum = 0.0
        for j in range(i, i + k):
            _sum += arr[j]
        result.append(_sum/k)
    return result


def main():
    result = find_averages_of_sub_arrays_bf(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))

    result = find_averages_of_sub_arrays_bf(2, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))

    return 0


main()
