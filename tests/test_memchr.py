from ctypes import c_int, c_size_t, c_void_p
from utils import libft

ft_memchr = libft.ft_memchr
memchr = libft.memchr
ft_memchr.argtypes = memchr.argtypes = (c_void_p, c_int, c_size_t)
ft_memchr.restype = memchr.restype = c_void_p


def test_memchr():
    data = (c_int * 2)(42, 512)
    for test in [0, 1, 2, 42, 258]:
        assert ft_memchr(data, test, 8) == memchr(data, test, 8)
