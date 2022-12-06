from ctypes import c_int
from utils import libft

ft_tolower = libft.ft_tolower
tolower = libft.tolower
ft_tolower.argtypes = tolower.argtypes = (c_int,)
ft_tolower.restype = ft_tolower.restype = c_int


def test_tolower():
    for i in range(256):
        assert ft_tolower(i) == tolower(i)
