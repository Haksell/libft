from ctypes import c_int
from utils import libft

ft_islower = libft.ft_islower
islower = libft.islower
ft_islower.argtypes = islower.argtypes = (c_int,)
ft_islower.restype = islower.restype = c_int


def test_islower():
    for i in range(256):
        assert bool(ft_islower(i)) == bool(islower(i))
