

def generate_all_substrings(str1):

    return [str1[i:j] for i in range(len(str1)) for j in range(i + 1, len(str1) + 1)]


def contains_no_repeat_chars(str1):
    d = {}
    for s in str1:
        d.setdefault(s, 0)
        d[s] += 1

    for s in str1:
        if d[s] != 1:
            return False

    return True


s = 'abcded'
l = 0
lst = generate_all_substrings(s)
for st1 in lst:
    if contains_no_repeat_chars(st1) is True:
        print(st1)
        l = max(l, len(st1))

print(l)
