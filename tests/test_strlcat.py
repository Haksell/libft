from ctypes import c_char_p, c_size_t, create_string_buffer
from string import ascii_lowercase
from utils import libft

ft_strlcat = libft.ft_strlcat
ft_strlcat.argtypes = (c_char_p, c_char_p, c_size_t)
ft_strlcat.restype = c_size_t

LOWER_BYTES = bytes(ascii_lowercase, "utf-8")


def compare(n):
    start = LOWER_BYTES[:6]
    end = LOWER_BYTES[6:]
    dest = create_string_buffer(50)
    dest.value = start
    src = create_string_buffer(end)
    ans = ft_strlcat(dest, src, n)
    assert ans == 20 + min(n, 6)
    assert dest.value == LOWER_BYTES[: max(6, n - 1)]


def test_smaller_dest():
    for i in range(7):
        compare(i)


def test_smaller_sum():
    for i in range(7, 27):
        compare(i)


def test_large_enough():
    for i in range(27, 60):
        compare(i)
