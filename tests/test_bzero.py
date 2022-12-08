from ctypes import addressof, create_string_buffer, c_int, c_void_p, c_size_t
from utils import libft

ft_bzero = libft.ft_bzero
ft_bzero.argtypes = (c_void_p, c_size_t)
ft_bzero.restype = None


def test_string():
    s1 = create_string_buffer(50)
    s1.value = b"This is not a test. Take cover."
    ft_bzero(addressof(s1) + 19, 7)
    assert s1.value == b"This is not a test."
    ft_bzero(addressof(s1) + 4, 7)
    assert s1.value == b"This"


def test_int():
    int_max = (1 << 31) - 1
    size = 10
    a1 = (c_int * size)(*([int_max] * size))
    ft_bzero(a1, 9)
    assert a1[0] == 0
    assert a1[1] == 0
    assert a1[2] == int_max - 255
    assert a1[3] == int_max
