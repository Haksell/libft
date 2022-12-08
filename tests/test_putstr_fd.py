from ctypes import c_char_p, c_int
from utils import libft
import os

ft_putstr_fd = libft.ft_putstr_fd
ft_putstr_fd.argtypes = (c_char_p, c_int)
ft_putstr_fd.restype = None

FILENAME = "tests/files/ft_putstr_fd"


def test_putstr_fd():
    with open(FILENAME, "w") as fp:
        fd = fp.fileno()
        ft_putstr_fd(b"first line", fd)
        ft_putstr_fd(b"\n", fd)
        ft_putstr_fd(b"second line", fd)
    assert open(FILENAME).read() == "first line\nsecond line"
    os.remove(FILENAME)
