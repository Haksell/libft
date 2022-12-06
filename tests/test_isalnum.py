from ctypes import c_int
from utils import libft

ft_isalnum = libft.ft_isalnum
isalnum = libft.isalnum
ft_isalnum.argtypes = isalnum.argtypes = (c_int,)
ft_isalnum.restype = ft_isalnum.restype = c_int


def test_isalnum():
    for i in range(256):
        assert bool(ft_isalnum(i)) == bool(isalnum(i))
