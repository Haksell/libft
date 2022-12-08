from ctypes import create_string_buffer, c_char_p, c_size_t
from utils import libft

ft_strchr = libft.ft_strchr
ft_strchr.argtypes = (c_char_p,)
ft_strchr.restype = c_size_t


def test_strchr():
    for b in (b"", b"a", b"ab", b"abc", b"abcd", b"abcde", b"ab\0cde"):
        sb = create_string_buffer(b)
        assert ft_strchr(sb) == libft.strchr(b)
