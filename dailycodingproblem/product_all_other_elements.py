## Problem 1.1 Get Product of all elements
def products(nums):
    prefix = []
    for n in nums:
        if prefix:
            prefix.append(prefix[-1] * n)
        else:
            prefix.append(n)
    print(prefix)

    suffix = []
    for n in reversed(nums):
        if suffix:
            suffix.append(suffix[-1]*n)
        else:
            suffix.append(n)
    suffix = list(reversed(suffix))
    print(suffix)

print(products([1, 2, 3, 4, 5]))
