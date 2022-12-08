from ctypes import c_char_p
from utils import libft

ft_strtrim = libft.ft_strtrim
ft_strtrim.argtypes = (c_char_p, c_char_p)
ft_strtrim.restype = c_char_p


def test_strtrim():
    assert ft_strtrim(b"a", b" \t\n") == b"a"
    assert ft_strtrim(b"   a", b" \t\n") == b"a"
    assert ft_strtrim(b"   a\t", b" \t\n") == b"a"
    assert ft_strtrim(b"   a\tlol", b" \t\n") == b"a\tlol"
    assert ft_strtrim(b"", b" \t\n") == b""
    assert ft_strtrim(b"aaaaaaaaaaaaa", b"a") == b""
    assert ft_strtrim(b" aaaa aaaaaaaaa", b"a") == b" aaaa "
