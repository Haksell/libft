from ctypes import CFUNCTYPE, c_char, c_char_p, c_uint
from utils import libft

func_type = CFUNCTYPE(c_char, c_uint, c_char)

ft_strmapi = libft.ft_strmapi
ft_strmapi.argtypes = (c_char_p, func_type)
ft_strmapi.restype = c_char_p


@func_type
def f_capitalize(i, c):
    return c.upper() if i == 0 else c.lower()


@func_type
def f_upper(_, c):
    return c.upper()


def test_capitalize():
    assert ft_strmapi(b"Comment SA VA???!!", f_capitalize) == b"Comment sa va???!!"
    assert ft_strmapi(b"wololo", f_capitalize) == b"Wololo"


def test_upper():
    assert ft_strmapi(b"Comment SA VA???!!", f_upper) == b"COMMENT SA VA???!!"
    assert ft_strmapi(b"wololo", f_upper) == b"WOLOLO"


def test_null():
    assert ft_strmapi(b"Comment SA VA???!!", func_type()) == b"Comment SA VA???!!"
    assert ft_strmapi(b"wololo", func_type()) == b"wololo"
