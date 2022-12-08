from ctypes import c_void_p, c_int, c_size_t
from utils import libft, same_sign

ft_memcmp = libft.ft_memcmp
memcmp = libft.memcmp
ft_memcmp.argtypes = memcmp.argtypes = (c_void_p, c_void_p, c_size_t)
ft_memcmp.restype = memcmp.restype = c_int


def test_memcmp():
    Pair = c_int * 2
    a1 = Pair(0, 0)
    a2 = Pair(0, 0)
    assert same_sign(ft_memcmp(a1, a2, 8), memcmp(a1, a2, 8))
    a1[1] = 256
    assert same_sign(ft_memcmp(a1, a2, 8), memcmp(a1, a2, 8))
    a2[1] = 42
    assert same_sign(ft_memcmp(a1, a2, 8), memcmp(a1, a2, 8))
    a1[1] = 42
    assert same_sign(ft_memcmp(a1, a2, 8), memcmp(a1, a2, 8))
    a1[0] = 12345
    assert same_sign(ft_memcmp(a1, a2, 8), memcmp(a1, a2, 8))
    a2[1] = 1234567
    assert same_sign(ft_memcmp(a1, a2, 8), memcmp(a1, a2, 8))
