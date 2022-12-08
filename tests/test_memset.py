from ctypes import addressof, create_string_buffer, c_int, c_size_t, c_void_p
from utils import libft

ft_memset = libft.ft_memset
ft_memset.argtypes = (c_void_p, c_int, c_size_t)
ft_memset.restype = c_void_p


def test_string():
    s1 = create_string_buffer(50)
    s1.value = b"This is not a test. Take cover."
    s2 = ft_memset(s1, ord("*"), 7)
    assert addressof(s1) == s2
    assert s1.value == b"******* not a test. Take cover."


def test_int():
    size = 10
    a1 = (c_int * size)(*([0] * size))
    a2 = ft_memset(a1, 42, 9)
    assert addressof(a1) == a2
    four_bytes_of_forty_two = 42 << 24 | 42 << 16 | 42 << 8 | 42
    assert a1[0] == four_bytes_of_forty_two
    assert a1[1] == four_bytes_of_forty_two
    assert a1[2] == 42
    assert a1[3] == 0
