from ctypes import c_char_p, c_int
from utils import libft
import os

ft_putendl_fd = libft.ft_putendl_fd
ft_putendl_fd.argtypes = (c_char_p, c_int)
ft_putendl_fd.restype = None

FILENAME = "tests/files/ft_putendl_fd"


def test_putendl_fd():
    with open(FILENAME, "w") as fp:
        fd = fp.fileno()
        ft_putendl_fd(b"yay", fd)
        ft_putendl_fd(b"", fd)
        ft_putendl_fd(b"nay", fd)
    assert open(FILENAME).read() == "yay\n\nnay\n"
    os.remove(FILENAME)
