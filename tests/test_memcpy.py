from ctypes import addressof, create_string_buffer, c_int, c_size_t, c_void_p
from utils import INT_MAX, libft

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
    size = 10
    ArrayTen = c_int * 10
    a1 = ArrayTen(*range(size))
    a2 = ArrayTen(*([INT_MAX] * size))
    a3 = ft_memcpy(a2, a1, 5)
    assert addressof(a2) == a3
    assert list(a2) == [
        0,
        INT_MAX - 254,
        INT_MAX,
        INT_MAX,
        INT_MAX,
        INT_MAX,
        INT_MAX,
        INT_MAX,
        INT_MAX,
        INT_MAX,
    ]


def test_null_null():
    assert ft_memcpy(None, None, 5) == None
