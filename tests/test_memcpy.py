from ctypes import *  # TODO
from utils import libft

ft_memcpy = libft.ft_memcpy
ft_memcpy.argtypes = (c_void_p, c_void_p, c_size_t)
ft_memcpy.restype = c_void_p


def test_string():
    s1 = create_string_buffer(50)
    s1.value = b"wolololololo"
    s2 = create_string_buffer(50)
    s2.value = b"zzzzzzzzzzzz"
    s3 = ft_memcpy(s2, s1, 5)
    assert s1.value == b"wolololololo"
    assert s2.value == b"wololzzzzzzz"
    assert addressof(s2) == s3


def test_int():
    int_max = (1 << 31) - 1
    size = 10
    ArrayTen = c_int * 10
    a1 = ArrayTen(*range(size))
    a2 = ArrayTen(*([int_max] * size))
    a3 = ft_memcpy(a2, a1, 5)
    assert addressof(a2) == a3
    assert list(a2) == [
        0,
        int_max - 254,
        int_max,
        int_max,
        int_max,
        int_max,
        int_max,
        int_max,
        int_max,
        int_max,
    ]


def test_null_null():
    assert ft_memcpy(None, None, 5) == None
