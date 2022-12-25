from ctypes import POINTER, c_bool, c_char_p, c_int, pointer
from utils import INT_MAX, INT_MIN, libft
from random import randint

ft_atoi_safe = libft.ft_atoi_safe
ft_atoi_safe.argtypes = (c_char_p, POINTER(c_int))
ft_atoi_safe.restype = c_bool


def check(s, target, should_be_safe):
    n = c_int()
    assert ft_atoi_safe(bytes(s, "utf-8"), pointer(n)) == should_be_safe
    if should_be_safe:
        assert n.value == target, (n.value, target)


def test_limits():
    for n in (INT_MIN, INT_MAX):
        check(str(n), n, True)


def test_small():
    for n in range(-42, 43):
        check(str(n), n, True)


def test_random():
    for _ in range(100):
        n = randint(INT_MIN, INT_MAX)
        check(str(n), n, True)


def test_bad_characters():
    for s in ["123.45", "+42", "    42", "0xff", "133t"]:
        check(s, None, False)


def test_overflow():
    for n in (INT_MIN - 1, INT_MAX + 1):
        check(str(n), None, False)
