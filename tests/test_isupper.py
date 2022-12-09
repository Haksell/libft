from ctypes import c_int
from utils import libft

ft_isupper = libft.ft_isupper
isupper = libft.isupper
ft_isupper.argtypes = isupper.argtypes = (c_int,)
ft_isupper.restype = ft_isupper.restype = c_int


def test_isupper():
    for i in range(256):
        assert bool(ft_isupper(i)) == bool(isupper(i))
