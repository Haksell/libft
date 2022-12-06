import ctypes
from main import libft
from random import randint

ft_atoi = libft.ft_atoi
ft_atoi.argtypes = (ctypes.c_char_p,)
ft_atoi.restypes = ctypes.c_int

INT_MAX = (1 << 31) - 1
INT_MIN = ~INT_MAX

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
