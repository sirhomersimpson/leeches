from non_repeat_substring import *


def test_non_repeat_substring():
    assert non_repeat_substring("aabccbb") == 3
    assert non_repeat_substring("abbbb") == 2
    assert non_repeat_substring("abccde") == 3


def test_is_unique():
    assert is_unique("aabccbb") == False
    assert is_unique("abc") == True
    assert is_unique("a") == True
    assert is_unique("") == True
