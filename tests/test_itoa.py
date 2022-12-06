from ctypes import c_char_p, c_int
from utils import libft
from random import randint

ft_itoa = libft.ft_itoa
ft_itoa.argtypes = (c_int,)
ft_itoa.restype = c_char_p

INT_MAX = (1 << 31) - 1
INT_MIN = ~INT_MAX


def compare(n):
    assert c_char_p(libft.ft_itoa(n)).value == bytes(str(n), "utf-8")


def test_limits():
    compare(INT_MIN)
    compare(INT_MAX)


def test_small():
    for i in range(-200, 201):
        compare(i)


def test_random():
    for _ in range(100):
        compare(randint(INT_MIN, INT_MAX))
