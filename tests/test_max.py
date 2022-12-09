from ctypes import c_int
from random import randint
from utils import INT_MAX, INT_MIN, libft

ft_max = libft.ft_max
ft_max.argtypes = (c_int, c_int)
ft_max.restype = c_int


def test_max():
    for _ in range(100):
        n1 = randint(INT_MIN, INT_MAX)
        n2 = randint(INT_MIN, INT_MAX)
        assert ft_max(n1, n2) == max(n1, n2)
