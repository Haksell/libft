from ctypes import c_char_p, c_ulong
from utils import libft
from random import randint

ft_itoa_base = libft.ft_itoa_base
ft_itoa_base.argtypes = (c_ulong, c_char_p)
ft_itoa_base.restype = c_char_p

ULONG_MAX = (1 << 64) - 1


def check(n):
    assert ft_itoa_base(n, b"0123456789abcdef") == bytes(hex(n)[2:], "utf-8")
    assert ft_itoa_base(n, b"0123456789") == bytes(str(n), "utf-8")
    assert ft_itoa_base(n, b"01") == bytes(bin(n)[2:], "utf-8")


def test_limits():
    check(0)
    check(ULONG_MAX)


def test_small():
    for i in range(1, 201):
        check(i)


def test_random():
    for _ in range(100):
        check(randint(0, ULONG_MAX))
