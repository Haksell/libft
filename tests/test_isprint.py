import ctypes
from utils import libft

ft_isprint = libft.ft_isprint
isprint = libft.isprint
ft_isprint.argtypes = isprint.argtypes = (ctypes.c_int,)
ft_isprint.restypes = ft_isprint.restypes = ctypes.c_int

def test_isprint():
    for i in range(256):
        assert bool(ft_isprint(i)) == bool(isprint(i))
