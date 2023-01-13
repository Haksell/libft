from ctypes import c_int
from utils import libft

ft_isspace = libft.ft_isspace
isspace = libft.isspace
ft_isspace.argtypes = isspace.argtypes = (c_int,)
ft_isspace.restype = isspace.restype = c_int


def test_isspace():
    for i in range(256):
        assert bool(ft_isspace(i)) == bool(isspace(i))
