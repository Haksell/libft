from ctypes import c_char_p, c_size_t, create_string_buffer
from utils import libft

ft_strlcpy = libft.ft_strlcpy
ft_strlcpy.argtypes = (c_char_p, c_char_p, c_size_t)
ft_strlcpy.restype = c_size_t


def compare(n):
    s = create_string_buffer(b"abcdefghijklmnopqrstuvwxyz")
    buffer = create_string_buffer(27)
    ans = ft_strlcpy(buffer, s, n)
    assert ans == 26
    assert buffer.value == (b"" if n == 0 else s.value[: n - 1])


def test_zero():
    compare(0)


def test_smaller():
    for i in range(1, 27):
        compare(i)


def test_same():
    compare(27)


def test_bigger():
    for i in range(27, 69):
        compare(i)
