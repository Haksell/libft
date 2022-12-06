from ctypes import c_int
from utils import libft

ft_toupper = libft.ft_toupper
toupper = libft.toupper
ft_toupper.argtypes = toupper.argtypes = (c_int,)
ft_toupper.restype = ft_toupper.restype = c_int


def test_toupper():
    for i in range(256):
        assert ft_toupper(i) == toupper(i)
