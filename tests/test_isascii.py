import ctypes
from utils import libft

ft_isascii = libft.ft_isascii
isascii = libft.isascii
ft_isascii.argtypes = isascii.argtypes = (ctypes.c_int,)
ft_isascii.restype = ft_isascii.restype = ctypes.c_int


def test_isascii():
    for i in range(256):
        assert bool(ft_isascii(i)) == bool(isascii(i))
