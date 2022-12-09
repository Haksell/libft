from ctypes import c_int
from random import randint
from utils import INT_MAX, INT_MIN, libft

ft_min = libft.ft_min
ft_min.argtypes = (c_int, c_int)
ft_min.restype = c_int


def test_min():
    for _ in range(100):
        n1 = randint(INT_MIN, INT_MAX)
        n2 = randint(INT_MIN, INT_MAX)
        assert ft_min(n1, n2) == min(n1, n2)
