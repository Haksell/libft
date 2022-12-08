from ctypes import addressof, create_string_buffer, c_char_p, c_size_t
from utils import libft

ft_strnstr = libft.ft_strnstr
ft_strnstr.argtypes = (c_char_p, c_char_p, c_size_t)
ft_strnstr.restype = c_size_t  # should be c_char_p but harder to test

HAYSTACK = create_string_buffer(b"abbccc")
EMPTY = create_string_buffer(b"")


def test_not_found():
    assert ft_strnstr(HAYSTACK, HAYSTACK, 0) == 0
    assert ft_strnstr(HAYSTACK, HAYSTACK, 5) == 0
    assert ft_strnstr(HAYSTACK, b"d", 5) == 0


def test_empty():
    assert ft_strnstr(HAYSTACK, EMPTY, 10) == addressof(HAYSTACK)
    assert ft_strnstr(EMPTY, HAYSTACK, 10) == 0
    assert ft_strnstr(EMPTY, EMPTY, 10) == addressof(EMPTY)


def test_found():
    assert ft_strnstr(HAYSTACK, HAYSTACK, 10) == addressof(HAYSTACK)
    assert ft_strnstr(HAYSTACK, HAYSTACK, 10) == addressof(HAYSTACK)
    assert ft_strnstr(HAYSTACK, b"bc", 10) == addressof(HAYSTACK) + 2
    assert ft_strnstr(HAYSTACK, b"c", 10) == addressof(HAYSTACK) + 3
    assert ft_strnstr(HAYSTACK, b"ccc", 10) == addressof(HAYSTACK) + 3
