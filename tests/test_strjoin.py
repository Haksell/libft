from ctypes import c_char_p
from utils import libft

ft_strjoin = libft.ft_strjoin
ft_strjoin.argtypes = (c_char_p, c_char_p)
ft_strjoin.restype = c_char_p


def test_strjoin():
    assert ft_strjoin(b"yolo", b"wesh") == b"yolowesh"
    assert ft_strjoin(b"yolo", b"") == b"yolo"
    assert ft_strjoin(b"", b"wesh") == b"wesh"
