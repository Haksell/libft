from ctypes import c_char_p, c_int
from utils import INT_MAX, INT_MIN, libft
from random import randint

ft_atoi = libft.ft_atoi
ft_atoi.argtypes = (c_char_p,)
ft_atoi.restype = c_int


def compare(n):
    assert libft.ft_atoi(bytes(str(n), "utf-8")) == n


def test_limits():
    compare(INT_MIN)
    compare(INT_MAX)


def test_small():
    for i in range(-200, 201):
        compare(i)


def test_random():
    for _ in range(100):
        compare(randint(INT_MIN, INT_MAX))


def test_spaces():
    assert ft_atoi(b"     42") == 42


def test_plus_minus():
    assert ft_atoi(b"+42") == 42
    assert ft_atoi(b"-42") == -42


def test_unrecognized():
    assert ft_atoi(b"   42  42") == 42
    assert ft_atoi(b"-42-42") == -42
    assert ft_atoi(b"12345qwert6789") == 12345
