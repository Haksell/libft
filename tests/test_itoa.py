from ctypes import c_char_p, c_int
from utils import INT_MAX, INT_MIN, libft
from random import randint

ft_itoa = libft.ft_itoa
ft_itoa.argtypes = (c_int,)
ft_itoa.restype = c_char_p


def check(n):
    assert ft_itoa(n) == bytes(str(n), "utf-8")


def test_limits():
    check(INT_MIN)
    check(INT_MAX)


def test_small():
    for i in range(-200, 201):
        check(i)


def test_random():
    for _ in range(100):
        check(randint(INT_MIN, INT_MAX))
