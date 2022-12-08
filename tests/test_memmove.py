from ctypes import addressof, create_string_buffer, c_size_t, c_void_p, memmove
from string import ascii_uppercase
from utils import libft

ft_memmove = libft.ft_memmove
ft_memmove.argtypes = (c_void_p, c_void_p, c_size_t)
ft_memmove.restype = c_void_p


def compare(offset1, offset2, n):
    s1 = create_string_buffer(bytes(ascii_uppercase, "utf-8"))
    addr1 = addressof(s1)
    memmove(addr1 + offset1, addr1 + offset2, n)
    s2 = create_string_buffer(bytes(ascii_uppercase, "utf-8"))
    addr2 = addressof(s2)
    memmove(addr2 + offset1, addr2 + offset2, n)
    assert s1.value == s2.value


def test_first_bigger():
    compare(5, 0, 10)


def test_second_bigger():
    compare(5, 10, 10)


def test_independent():
    compare(5, 20, 10)


def test_null_null():
    assert ft_memmove(None, None, 5) == None
