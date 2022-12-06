from ctypes import c_int
from utils import libft

ft_isascii = libft.ft_isascii
isascii = libft.isascii
ft_isascii.argtypes = isascii.argtypes = (c_int,)
ft_isascii.restype = ft_isascii.restype = c_int


def test_isascii():
    for i in range(256):
        assert bool(ft_isascii(i)) == bool(isascii(i))
