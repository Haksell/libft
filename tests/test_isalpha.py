import ctypes
from utils import libft

ft_isalpha = libft.ft_isalpha
isalpha = libft.isalpha
ft_isalpha.argtypes = isalpha.argtypes = (ctypes.c_int,)
ft_isalpha.restypes = ft_isalpha.restypes = ctypes.c_int

def test_isalpha():
    for i in range(256):
        assert bool(ft_isalpha(i)) == bool(isalpha(i))
