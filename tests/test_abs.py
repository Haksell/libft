from ctypes import c_int
from random import randint
from utils import INT_MAX, INT_MIN, libft

ft_abs = libft.ft_abs
ft_abs.argtypes = (c_int,)
ft_abs.restype = c_int


def test_abs():
    for _ in range(100):
        n = randint(INT_MIN, INT_MAX)
        assert ft_abs(n) == abs(n)
