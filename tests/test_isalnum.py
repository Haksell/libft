import ctypes
from main import libft

ft_isalnum = libft.ft_isalnum
isalnum = libft.isalnum
ft_isalnum.argtypes = isalnum.argtypes = (ctypes.c_int,)
ft_isalnum.restypes = ft_isalnum.restypes = ctypes.c_int

def test_isalnum():
    for i in range(256):
        assert bool(ft_isalnum(i)) == bool(isalnum(i))
