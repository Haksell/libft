from ctypes import addressof, create_string_buffer, c_int, c_void_p, c_size_t
from utils import INT_MAX, libft

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
    size = 10
    a1 = (c_int * size)(*([INT_MAX] * size))
    ft_bzero(a1, 9)
    assert a1[0] == 0
    assert a1[1] == 0
    assert a1[2] == INT_MAX - 255
    assert a1[3] == INT_MAX
