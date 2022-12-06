import ctypes
from utils import libft

ft_isdigit = libft.ft_isdigit
isdigit = libft.isdigit
ft_isdigit.argtypes = isdigit.argtypes = (ctypes.c_int,)
ft_isdigit.restypes = ft_isdigit.restypes = ctypes.c_int

def test_isdigit():
    for i in range(256):
        assert bool(ft_isdigit(i)) == bool(isdigit(i))
