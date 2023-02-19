from ctypes import c_char_p
from utils import libft

ft_strjoin3 = libft.ft_strjoin3
ft_strjoin3.argtypes = (c_char_p, c_char_p)
ft_strjoin3.restype = c_char_p


def test_strjoin3():
    assert ft_strjoin3(b"a", b"b", b"c") == b"abc"
    assert ft_strjoin3(b"a", b"", b"bc") == b"abc"
    assert ft_strjoin3(b"", b"", b"abc") == b"abc"
