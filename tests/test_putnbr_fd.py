from ctypes import c_int
from random import randint
from test_putchar_fd import ft_putchar_fd
from utils import INT_MAX, INT_MIN, libft
import os

ft_putnbr_fd = libft.ft_putnbr_fd
ft_putnbr_fd.argtypes = (c_int, c_int)
ft_putnbr_fd.restype = c_int

FILENAME = "tests/files/ft_putnbr_fd"


def check(nums):
    with open(FILENAME, "w") as fp:
        fd = fp.fileno()
        for n in nums:
            assert ft_putnbr_fd(n, fd) == len(str(fd))
            ft_putchar_fd(ord("\n"), fd)
    assert open(FILENAME).read() == "".join(f"{n}\n" for n in nums)
    os.remove(FILENAME)


def test_limits():
    check([INT_MIN, INT_MAX])


def test_small():
    check(list(range(-200, 201)))


def test_random():
    check([randint(INT_MIN, INT_MAX) for _ in range(100)])
