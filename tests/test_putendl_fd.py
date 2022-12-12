from ctypes import c_char_p, c_int
from utils import libft
import os

ft_putendl_fd = libft.ft_putendl_fd
ft_putendl_fd.argtypes = (c_char_p, c_int)
ft_putendl_fd.restype = c_int

FILENAME = "tests/files/ft_putendl_fd"


def test_putendl_fd():
    with open(FILENAME, "w") as fp:
        fd = fp.fileno()
        assert ft_putendl_fd(b"yay", fd) == 4
        assert ft_putendl_fd(b"", fd) == 1
        assert ft_putendl_fd(b"nay", fd) == 4
    assert open(FILENAME).read() == "yay\n\nnay\n"
    os.remove(FILENAME)
