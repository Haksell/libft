from ctypes import c_char_p, c_uint, c_size_t
from utils import libft

ft_substr = libft.ft_substr
ft_substr.argtypes = (c_char_p, c_uint, c_size_t)
ft_substr.restype = c_char_p


def test_after():
    assert ft_substr(b"yolowesh", 8, 3) == b""
    assert ft_substr(b"yolowesh", 10, 3) == b""


def test_truncated():
    assert ft_substr(b"yolowesh", 3, 8) == b"owesh"
    assert ft_substr(b"yolowesh", 7, 8) == b"h"


def test_normal():
    assert ft_substr(b"yolowesh", 3, 5) == b"owesh"
    assert ft_substr(b"yolowesh", 0, 8) == b"yolowesh"
    assert ft_substr(b"yolowesh", 0, 2) == b"yo"
    assert ft_substr(b"", 0, 0) == b""
