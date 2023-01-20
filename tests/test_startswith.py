from ctypes import c_bool, c_char_p
from utils import libft

ft_startswith = libft.ft_startswith
ft_startswith.argtypes = ft_startswith.argtypes = (c_char_p, c_char_p)
ft_startswith.restype = ft_startswith.restype = c_bool


def test_true():
    assert ft_startswith(b"wololo", b"")
    assert ft_startswith(b"wololo", b"w")
    assert ft_startswith(b"wololo", b"wo")
    assert ft_startswith(b"wololo", b"wol")
    assert ft_startswith(b"wololo", b"wololo")


def test_false():
    assert not ft_startswith(b"", b"wo")
    assert not ft_startswith(b"wololo", b"z")
    assert not ft_startswith(b"wololo", b"woo")
    assert not ft_startswith(b"wololo", b"wololol")
