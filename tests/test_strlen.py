from ctypes import create_string_buffer, c_char_p, c_size_t
from utils import libft

ft_strlen = libft.ft_strlen
ft_strlen.argtypes = (c_char_p,)
ft_strlen.restype = c_size_t


def test_strlen():
    for b in (b"", b"a", b"ab", b"abc", b"abcd", b"abcde", b"ab\0cde"):
        assert ft_strlen(b) == libft.strlen(b)
