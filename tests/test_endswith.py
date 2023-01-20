from ctypes import c_bool, c_char_p
from utils import libft

ft_endswith = libft.ft_endswith
ft_endswith.argtypes = ft_endswith.argtypes = (c_char_p, c_char_p)
ft_endswith.restype = ft_endswith.restype = c_bool


def test_true():
    assert ft_endswith(b"wololo", b"")
    assert ft_endswith(b"wololo", b"o")
    assert ft_endswith(b"wololo", b"lo")
    assert ft_endswith(b"wololo", b"olo")
    assert ft_endswith(b"wololo", b"wololo")


def test_false():
    assert not ft_endswith(b"", b"wo")
    assert not ft_endswith(b"wololo", b"l")
    assert not ft_endswith(b"wololo", b"lol")
    assert not ft_endswith(b"wololo", b"owololo")
