from ctypes import c_char, c_int
from utils import libft
import os

ft_putchar_fd = libft.ft_putchar_fd
ft_putchar_fd.argtypes = (c_char, c_int)
ft_putchar_fd.restype = c_int

FILENAME = "tests/files/ft_putchar_fd"


def test_putchar_fd():
    with open(FILENAME, "w") as fp:
        fd = fp.fileno()
        for c in "ft_putchar_fd":
            assert ft_putchar_fd(ord(c), fd) == 1
    assert open(FILENAME).read() == "ft_putchar_fd"
    os.remove(FILENAME)
